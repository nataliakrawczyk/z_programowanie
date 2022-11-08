import csv
from io import TextIOWrapper;
import json
from flask import Flask
from flask import jsonify

csvTags = open('tags.csv', 'r', encoding = "UTF-8")

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.moveId = movieId
        self.tag = tag
        self.timestamp = timestamp

def getTagsList(file: TextIOWrapper) -> list:
    tagsList = []
    file.__next__()
    for tag in file.readlines():
        tagAttributes = tag.replace('\n', '').split(',')
        objectTag = Tag(tagAttributes[0], tagAttributes[1], tagAttributes[2], tagAttributes[3])
        tagsList.append(objectTag.__dict__)
    return tagsList

app = Flask(__name__)

tagsList = getTagsList(csvTags)

@app.route('/tags', methods = ["GET"], )
def index():
    return jsonify(tagsList)

app.run()