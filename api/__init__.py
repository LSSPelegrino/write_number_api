"""
Initialize API Module
"""

# # 3rd Party Modules
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.url_map.strict_slashes = False

api = Api(app, catch_all_404s=True)

# # Recursive Imports
from api import errors, calls
