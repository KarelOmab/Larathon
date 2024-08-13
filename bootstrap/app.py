import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Set up the configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('DB_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize extensions
db = SQLAlchemy(app)

# Import routes (so they are registered with the app)
#from app.Http import routes

# Import models (if necessary)
#from app.Models import User  # Ensure this is imported for use with db.create_all() etc.
