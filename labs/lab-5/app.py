"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bad1')
def bad1():
    return render_template("bad1.html")

@app.route('/mightSpace_help')
def mightSpace_help():
    return render_template("mightSpace_help.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

@app.route('/bad4')
def bad4():
    return render_template("bad4.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

