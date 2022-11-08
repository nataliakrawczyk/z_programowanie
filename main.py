from flask import Flask
from links import links_api
from movie import movie_api
from ratings import ratings_api
from tags import tags_api

app = Flask(__name__)

app.register_blueprint(links_api)
app.register_blueprint(movie_api)
app.register_blueprint(ratings_api)
app.register_blueprint(tags_api)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def index():
    return """<h1>Endpoints to use:</h1>
    <br/><h2>/links</h2>
    <br/><h2>/movies</h2>
    <br/><h2>/ratings</h2>
    <br/><h2>/tags</h2>
"""

if __name__ == "__main__":
    app.run()