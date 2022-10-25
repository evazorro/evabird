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
    return render_template('index.html')

@app.route('/regions/<region>')
def regional_sightings(region):
    birds = get_recent_notable_birds(region)
    region_name = get_region_detail(region)
    return render_template('birds.html', region_name=region_name, birds=birds)