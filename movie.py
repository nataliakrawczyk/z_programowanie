from flask import Blueprint, jsonify
import pandas as pd

movie_api = Blueprint('movie_api', __name__)
csvMovies = pd.DataFrame.transpose(pd.read_csv('movies.csv', header=None))

class Movie: 
    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

def getMovieList() -> list:
    movieList = []
    for index in range(1, csvMovies.shape[1]):
        movieAttributes = csvMovies[index]
        objectMovie = Movie(movieAttributes[0], movieAttributes[1], movieAttributes[2])
        movieList.append(objectMovie.__dict__)
    return movieList

movieList = getMovieList()

@movie_api.route('/movies', methods=["GET"], )
def movies():
    return jsonify(movieList)

