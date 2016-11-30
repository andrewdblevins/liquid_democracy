###
# Liquid Democracy API
# using pagerank to find the most trusted decision makers
#
# Andrew Blevins and Hyatt Baily
###
import numpy as np
from scipy import linalg,sparse

from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

users = []
connections = []

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def handle_users():    
    if request.method == 'POST':
        user = request.get_json(force=True)
	print user
	users.append(user)
        return jsonify({'status':'success'}), 201
    else:
        return str(users) 

@app.route('/connections', methods=['GET', 'POST'])
def handle_connections():
    if request.method == 'POST':
        connection = request.get_json(force=True)
        print connection
        if connection[0] in users and connection[1] in users:
            connections.append(connection)
            return jsonify({'status':'success'}), 201
        else:
            print('I dont recognize that person')
            return jsonify({'status':'failure'}), 403
    else:
        return str(connections)
 
@app.route('/trust')
def handle_trust():
    trust_matrix = np.array([[1, 0],
              	            [.5,.5]])
    eigen_values,trust_vector = linalg.eig(trust_matrix) 
    return str(eigen_values), str(trust_vector)

if __name__ == '__main__':
    app.run(debug=True)
