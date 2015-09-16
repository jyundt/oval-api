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
    if 'year' in request.args and not request.args['year'].isdigit():
        return jsonify({'code': 400, 'message': "Invalid year.", 'fields': 'year'}), 400

    
    json_result = []
    for race in db.races.find({},{"_id": 0}).limit(0):
        json_result.append(race)
    return jsonify({"races": json_result})
@app.route('/categories')
def get_categores():
    if 'year' in request.args and not request.args['year'].isdigit():
        return jsonify({'code': 400, 'message': "Invalid year.", 'fields': 'year'}), 400
    if 'year' in request.args:
        start_date = datetime.datetime(int(request.args['year']),1,1)
        end_date = datetime.datetime(int(request.args['year']),12,31)
        return jsonify({'categories': races.distinct('category',{ "date": {"$gte": start_date, "$lt": end_date }})})
    else:
        return jsonify({'categories': races.distinct('category')})

@app.route('/test')
def test():
    return "Value for year: " + request.args.get('year', 'HELLO!')
if __name__ == '__main__':
    app.run(debug=True)
