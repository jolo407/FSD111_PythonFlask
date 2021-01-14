"""Module init file"""

from flask import Flask
#from flask_boostrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)
#app.config["SECRET_KEY"] = "MYSUPERSECRETSTRING"

from app import routes