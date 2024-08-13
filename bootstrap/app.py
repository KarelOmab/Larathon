import os
import sys
from flask import Flask
from dotenv import load_dotenv
from database import db  # Adjusted import path to match the correct location

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__, template_folder='../resources/templates')

# Set up the configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('DB_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Adjust the Python path to include the directory above 'bootstrap'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Bind the db to the app
db.init_app(app)

# Import routes from web.py and register the blueprint
from routes.web import app as routes_app
app.register_blueprint(routes_app)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=5001)

