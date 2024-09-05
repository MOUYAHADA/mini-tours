from flask import Flask, render_template, request, redirect
from datetime import date
from math import ceil
import json, re

app = Flask(__name__)


with open('data/tours.json') as tours_file:
    all_tours = json.load(tours_file)
    tours_count = len(all_tours)
    page_count = ceil(tours_count/10)
    total_items = len(all_tours)
    
with open('data/descriptions.json') as d_file:
    descriptions = json.load(d_file)
    
with open('data/destinations.json') as destinations_file:
    all_destinations = json.load(destinations_file)

def get_pages(total_items):
    page_number = request.args.get('page', 1, type=int)

    if page_number < 1 or page_number > total_items // 10 + (1 if total_items % 10 > 0 else 0):
        page_number = 1

    limit = page_number * 10
    start = limit - 10
    return start, limit, page_number

@app.context_processor
def inject_year():
    return { 'year' : date.today().year }

@app.get('/', strict_slashes=False)
def index():
    tours = all_tours[0:3]
    return render_template('index.html', tours=tours)


@app.get('/tours/', strict_slashes=False)
def tours():
    search_value = request.args.get('search', '').strip()

    filtered_tours = [
        item for item in all_tours 
        if (search_value.lower() in item.get('name', '').lower() or 
            search_value.lower() in item.get('description', '').lower())
    ]

    total_filtered_tours = len(filtered_tours)

    start, limit, page_count = get_pages(total_filtered_tours)

    paginated_tours = filtered_tours[start:limit]

    return render_template('tours.html', 
                           tours=paginated_tours, 
                           page_count=page_count, 
                           search_value=search_value)

@app.get('/tours/<slug>', strict_slashes=False)
def tour(slug):
    tour = [item for item in all_tours if item.get('slug') == slug]
    if len(tour) == 0:
        return redirect('/tours')
    description = [item for item in descriptions if item.get('id') == tour[0].get('id')][0]
    return render_template('tour.html',
                           tour=tour[0], 
                           description=description)

@app.get('/destinations', strict_slashes=False)
def destinations():
    return render_template('destinations.html',
                           destinations=all_destinations)
    
@app.get('/destinations/<name>', strict_slashes=False)
def destination(name):
    destination_tours = [item for item in all_tours if name in item.get('slug').split('-')]
    start, limit, page_count = get_pages()
    return render_template('tours.html',
                           tours=destination_tours[start:limit], page_count=page_count)

@app.get('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)