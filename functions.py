"""Module for utility functions"""
from bleach import clean
import json

def store_as_json(data, filename):
    """Store a Python object as a JSON file."""
    try:
        with open(filename, 'a') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

def read_from_json(filename):
    """Read a JSON file and return the corresponding Python object."""
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"An error occurred while reading from {filename}: {e}")
        return None
    
def save_message(name, email, subject, message):
    """Stores a message to local json file"""
    allowed_tags = ['b', 'i', 'u']
    data = {
        "name": clean(name),
        "email": clean(email),
        "subject": clean(subject),
        "message": clean(message, tags=allowed_tags)
        }
    store_as_json(data, 'messages.json')

def save_booking(name, email, participants, date, tour):
    """Stores booking to local file"""
    allowed_tags = ['b', 'i', 'u']
    data = {
        "name": clean(name),
        "email": clean(email),
        "participants": clean(participants),
        "date": clean(date),
        "tour": tour
        }
    store_as_json(data, 'data/messages.json')

def get_messages():
    """get all messages from json file"""
    read_from_json('data/messages.json')

def get_bookings():
    """get all bookings from json file"""
    read_from_json('data/messages.json')