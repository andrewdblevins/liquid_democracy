###
# Liquid Democracy API
# using pagerank to find the most trusted decision makers
#
# Andrew Blevins and Hyatt Baily
###
import numpy as np
from scipy import linalg,sparse
from collections import namedtuple

from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

User = namedtuple('User', ['name'], verbose=True)
users = []

Connection = namedtuple('Connection', ['source', 'target'], verbose=True)
connections = []

class TrustMatrix():
    def __init__(self,users,connections):
        self.users = users 
        self.connections = connections 

        num_users = len(users)
	self.trust =  np.ones((num_users,num_users))
        for connection in self.connections:
            source_index = users.index(connection.source)
            target_index = users.index(connection.target)
            self.trust[source_index][target_index] = 100

        self.trust = self.normalize()

    def normalize(self):
    	row_sums = self.trust.sum(axis=1)
	return self.trust / row_sums[:, np.newaxis]

    def evaluate(self):
        _,eigen_vectors = linalg.eig(self.trust)
        for i,t in enumerate(eigen_vectors):
            print users[i].name+': '+str(t)

def read_user(user_json):
    if 'name' in user_json.keys():
        user = User(name=user_json['name'])
    	return user



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def handle_users():    
    if request.method == 'POST':
        user = read_user(request.get_json(force=True))
        if user not in users:
	    users.append(user)
            return jsonify({'status':'success'}), 201
        else:
            return jsonify({'status':'failure'}), 403 
    else:
        return str(users) 

@app.route('/connections', methods=['GET', 'POST'])
def handle_connections():
    if request.method == 'POST':
        connection_json = request.get_json(force=True)
        connection = Connection(source=read_user(connection_json['source']),target=read_user(connection_json['target']))
        if connection.source in users and connection.target in users and connection not in connections:
            connections.append(connection)
            return jsonify({'status':'success'}), 201
        else:
            print('I dont recognize that person')
            return jsonify({'status':'failure'}), 403
    else:
        return str(connections)
 
@app.route('/trust')
def handle_trust():
    trust = TrustMatrix(users,connections)
    return str(trust.evaluate())


if __name__ == '__main__':
    app.run(debug=True)
