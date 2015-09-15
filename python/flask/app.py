#!/usr/bin/python
from pymongo import MongoClient
from flask import Flask, jsonify, request
import datetime

#define our mongo connection
client = MongoClient("localhost", 27017)
db = client.oval
races = db.races


app = Flask(__name__)

@app.route('/')
def index():
    return "oval api"

@app.route('/races')
def get_races():
	json_result = []
	for race in db.races.find({},{"_id": 0}).limit(0):
		json_result.append(race)
	return jsonify({"races": json_result})
@app.route('/categories')
def get_categores():
	if 'year' in request.args:
		#return 'Categories for ' + request.args['year']
		return jsonify({'categories': races.distinct('category',{ "date": {"$gte": datetime.datetime(2015,1,1), "$lt": datetime.datetime(2015,12,31)}})})
	else:
		#return 'Categories'	
		return jsonify({'categories': races.distinct('category')})

@app.route('/test')
def test():
	return "Value for year: " + request.args.get('year', 'HELLO!')
if __name__ == '__main__':
    app.run(debug=True)
