import csv
from io import TextIOWrapper;
import json
from flask import Flask
from flask import jsonify

csvRatings = open('ratings.csv', 'r', encoding = "UTF-8")

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.moveId = movieId
        self.rating = rating
        self.timestamp = timestamp

def getRatingsList(file: TextIOWrapper) -> list:
    ratingsList = []
    file.__next__()
    for rating in file.readlines():
        ratingAttributes = rating.replace('\n', '').split(',')
        objectRating = Rating(ratingAttributes[0], ratingAttributes[1], ratingAttributes[2], ratingAttributes[3])
        ratingsList.append(objectRating.__dict__)
    return ratingsList

app = Flask(__name__)

ratingList = getRatingsList(csvRatings)

@app.route('/ratings', methods = ["GET"], )
def index():
    return jsonify(ratingList)

app.run()