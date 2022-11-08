import csv
from io import TextIOWrapper;
import json
from flask import Flask
from flask import jsonify

csvMovies = open('movies.csv', 'r', encoding = "UTF-8")

class Movie:
    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

def getMovieList(file: TextIOWrapper) -> list:
    movieList = []
    file.__next__()
    for movie in file.readlines():
        movieAttributes = movie.split(',')
        objectMovie = Movie(movieAttributes[0], movieAttributes[1], movieAttributes[2].replace("\n", ''))
        movieList.append(objectMovie.__dict__)
    return movieList

app = Flask(__name__)

movieList = getMovieList(csvMovies)

@app.route('/movies', methods = ["GET"], )
def index():
    return jsonify(movieList)

app.run()