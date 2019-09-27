"""
Implement API calls
"""

# # 3rd Party Modules
from flask import jsonify
from flask_restful import Resource

# # Internal Modules
from api import api
from api.errors import bad_request
from cardinals import to_cardinal_number
from config import MAX_RANGE


class ApiCardinalNumber(Resource):
    """
    Defines resource class for cardinal numbers transformation
    """
    def get(self, number):
        """
        Implement GET method
        """
        if abs(number) > MAX_RANGE:
            return bad_request(
                f"The number must be in the -{MAX_RANGE} "
                f"and {MAX_RANGE} range"
            )
        data = {
            "extenso": to_cardinal_number(number)
        }
        return jsonify(data)


api.add_resource(ApiCardinalNumber, '/<int(signed=True):number>')
