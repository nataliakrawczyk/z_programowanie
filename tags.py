from flask import jsonify, Blueprint
import pandas as pd

tags_api = Blueprint('tags_api', __name__)

csvTags = pd.DataFrame.transpose(pd.read_csv('tags.csv'))

class Tag: 
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.moveId = movieId
        self.tag = tag
        self.timestamp = timestamp

def getTagsList() -> list:
    tagsList = []
    for index in range(1, csvTags.shape[1]):
        tagAttributes = csvTags[index]
        objectTag = Tag(tagAttributes[0], tagAttributes[1], tagAttributes[2], tagAttributes[3])
        tagsList.append(objectTag.__dict__)
    return tagsList

tagsList = getTagsList()

@tags_api.route('/tags', methods=["GET"], )
def tags():
    return jsonify(tagsList)