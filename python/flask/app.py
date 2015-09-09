#!/usr/bin/python
import pymongo
from flask import Flask, jsonify, request

#define our mongo connection
client = pymongo.MongoClient("localhost", 27017)
db = client.oval

db.name

app = Flask(__name__)

@app.route('/')
def index():
    return "oval api"

@app.route('/categories')
def get_categores():
	if 'year' in request.args:
		return 'Categories for ' + request.args['year']
	else:
		return 'Categories'	

if __name__ == '__main__':
    app.run(debug=True)
