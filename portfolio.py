#!/usr/bin/env python3
from flask import Flask
#'flask run' in the terminal will run the final version
#'./portfolio will run in degbug mode'
app = Flask(__name__)

@app.route('/')
@app.route('home')
def home():
    return '<h1>Homepage</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

#This is to get live updates-- debugger mode
if __name__ == '__main__':
    app.run(debug=True)
