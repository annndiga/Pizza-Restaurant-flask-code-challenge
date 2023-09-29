# app.py
from flask import Flask
from flask_cors import CORS
from models.dbconfig import db  # Import the db object
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'  # Replace with your actual database URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
