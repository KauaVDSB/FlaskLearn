from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sql_migrate import Migrate


app = Flask(__name__)




from flaskLearn.routes import homepage