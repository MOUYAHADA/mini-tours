from flask import Flask, render_template, url_for
from datetime import date
import json

app = Flask(__name__)

with open('data/tours.json') as tours_file:
    all_tours = json.load(tours_file)

@app.context_processor
def inject_year():
    return { 'year' : date.today().year }

@app.get('/', strict_slashes=False)
def index():
    tours = all_tours[0:3]
    return render_template('index.html', tours=tours)

@app.get('/tours/<slug>', strict_slashes=False)
def tour(slug):
    tour = [item for item in all_tours if item.get('slug') == slug][0]
    return render_template('tour.html', tour=tour)

@app.get('/tours/', strict_slashes=False)
def tours():
    return render_template('tours.html', tours=all_tours)

@app.get('/destinations', strict_slashes=False)
def destinations():
    return render_template('destinations.html')

@app.get('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)