from flask import Flask
from .config import DevConfig



app = Flask(__name__ ,instance_relative_config = True)

app.config.from_object(DevConfig)

from app import views