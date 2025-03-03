from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'kjsxhiqwhe2kjh2A-9d8hwd!!noi1d9hd918his21ioj9821j'

db = SQLAlchemy(app)
migrate = Migrate(app, db)




from flaskLearn.routes import homepage
from flaskLearn.models import Contato