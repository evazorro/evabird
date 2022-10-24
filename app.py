import re
from flask import Flask, render_template
from get_recent_notable_birds import get_recent_notable_birds

app = Flask(__name__)

@app.route('/')
def index():
    birds = get_recent_notable_birds()
    return render_template('birds.html', birds=birds)

@app.route('/<name>')
def hello_world(name):
    return render_template('hello.html.j2', name=name)