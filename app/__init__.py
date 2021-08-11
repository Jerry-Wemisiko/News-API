from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootsrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__ )

    #flask extensions
    bootsrap.init_app(app)

    return app