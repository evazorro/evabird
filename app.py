import re
from flask import Flask, render_template, request, redirect, url_for
from get_recent_notable_birds import get_recent_notable_birds
from get_region_detail import get_region_detail

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        region=request.form.get('region')
        return redirect(url_for('regional_sightings', region=region))
    return render_template('index.html.j2')

@app.route('/regions/<region>')
def regional_sightings(region):
    birds = get_recent_notable_birds(region) # should this logic happen elsewhere?
    region_name = get_region_detail(region)
    return render_template('birds.html.j2', region_name=region_name, birds=birds)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html.j2'), 404