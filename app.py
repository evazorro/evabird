import re
from flask import Flask, render_template, request, redirect, url_for
from get_recent_notable_birds import get_recent_notable_birds

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        region=request.form['region']
        return redirect(url_for(region)) # todo, debug this
    return render_template('index.html')

@app.route('/<region>')
def regional_sightings(region):
    birds = get_recent_notable_birds(region)
    return render_template('birds.html', region=region, birds=birds)