#!/usr/bin/env python3
''' Task 0 - basic flask app
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ''' The Default route '''
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
