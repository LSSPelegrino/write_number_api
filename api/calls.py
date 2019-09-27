"""
Implement API calls
"""

# # 3rd Party Modules
from flask import jsonify
from flask_restful import Resource

# # Internal Modules
from api import api
from cardinals import to_cardinal_number


class ApiCardinalNumber(Resource):
    """
    Defines resource class for cardinal numbers transformation
    """
    def get(self, number):
        """
        Implement GET method
        """
        data = {
            "extenso": to_cardinal_number(number)
        }
        return jsonify(data)


api.add_resource(ApiCardinalNumber, '/<int(signed=True):number>')
