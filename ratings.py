import pandas as pd
from flask import Flask, Blueprint, jsonify

ratings_api = Blueprint('ratings_api', __name__)

csvRatings = pd.DataFrame.transpose(pd.read_csv('ratings.csv'))

class Rating: 
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.moveId = movieId
        self.rating = rating
        self.timestamp = timestamp

def getRatingsList() -> list:
    ratingsList = []
    for index in range(1, csvRatings.shape[1]):
        ratingAttributes = csvRatings[index]
        objectRating = Rating(ratingAttributes[0], ratingAttributes[1], ratingAttributes[2], ratingAttributes[3])
        ratingsList.append(objectRating.__dict__)
    return ratingsList

ratingList = getRatingsList()

@ratings_api.route('/ratings', methods=["GET"], )
def ratings():
    return jsonify(ratingList)
