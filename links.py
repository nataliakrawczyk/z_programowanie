from flask import Blueprint, jsonify
import pandas as pd

links_api = Blueprint('links_api', __name__)

csvLinks = pd.DataFrame.transpose(pd.read_csv('links.csv'))

class Link: 
    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

def getLinksList() -> list:
    linksList = []
    for index in range(1, csvLinks.shape[1]):
        linkAttributes = csvLinks[index]
        objectLink = Link(linkAttributes[0], linkAttributes[1], linkAttributes[2])
        linksList.append(objectLink.__dict__)
    return linksList

movieList = getLinksList()

@links_api.route('/links', methods=["GET"], )
def links():
    return jsonify(movieList)