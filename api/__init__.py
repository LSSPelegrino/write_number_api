"""
Initialize API Module
"""

# # 3rd Party Modules
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

# # Recursive Imports
from api import app, errors, calls
