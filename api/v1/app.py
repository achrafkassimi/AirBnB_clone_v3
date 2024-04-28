#!/usr/bin/python3
""" Flask Application """
from models import storage
from flask import Flask
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == "__main__":
    """ Main Function """
    # host = getenv('HBNB_API_HOST')
    # port = getenv('HBNB_API_PORT')
    # if not host:
    #     host = '0.0.0.0'
    # if not port:
    #     port = '5000'

    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
