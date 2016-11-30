###
# Liquid Democracy API
# using pagerank to find the most trusted decision makers
#
# Andrew Blevins and Hyatt Baily
###
from scipy import linalg

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users')
def users():
    return "[1, 2, 3]"

@app.route('/connections')
def connections():
    return "[1, 2, 3]"

@app.route('/trust')
def connections():
    return "[1, 2, 3]"

if __name__ == '__main__':
    app.run()
