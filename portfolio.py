#!/usr/bin/env python3
from flask import Flask, render_template, url_for
import getRepos

#'flask run' in the terminal will run the final version
#'./portfolio will run in degbug mode'
app = Flask(__name__)


projects = getRepos.handleData()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', projects=projects, title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title='About')

#This is to get live updates-- debugger mode
if __name__ == '__main__':
    app.run(debug=True)
