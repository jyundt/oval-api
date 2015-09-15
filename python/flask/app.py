#!/usr/bin/python
from pymongo import MongoClient
from flask import Flask, jsonify, request

#define our mongo connection
client = MongoClient("localhost", 27017)
db = client.oval
races = db.races



app = Flask(__name__)

@app.route('/')
def index():
    return "oval api"

@app.route('/categories')
def get_categores():
	if 'year' in request.args:
		#return 'Categories for ' + request.args['year']
		return jsonify({'categories': races.distinct('category',{ "date": {"$gte": "new Date(2015,1,1)", "$lt": "new Date(2015,12,31)"}})})
	else:
		#return 'Categories'	
		return jsonify({'categories': races.distinct('category')})

if __name__ == '__main__':
    app.run(debug=True)
