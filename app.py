from typing import reveal_type
from config import config
from flask import Flask
from routes import Movie

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not Found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    # Blue
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
