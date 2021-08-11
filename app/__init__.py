from flask import Flask
from flask_bootsrap import Bootstrap



app = Flask(__name__ ,instance_relative_config = True)

#flask extensions
bootsrap = Bootstrap(app)

from app import views