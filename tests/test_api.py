"""
Test cases to the API module.
Call these tests on the command line at project root using:
    $ python -m unittest tests.test_api
"""

# # Standard Modules
from unittest import TestCase

# # 3rd Party Modules
import json
# from werkzeug.http import HTTP_STATUS_CODES

# # Internal Modules
import write_number_api as api_to_test
# from api.errors import bad_request
# from api.errors import error_response
from .test_variables import INT_VALUE_PAIRS
from .test_variables import BAD_VALUES_INT
from .test_variables import BAD_TYPES_NO_INT


# class TestApiErrors(TestCase):
#     """
#     Tests the api.errors module
#     """
#     def setUp(self):
#         """
#         Sets up the test variables
#         """
#         # api_to_test.app.testing = True
#         # self.app = api_to_test.app.test_client()

#     def test_output(self):
#         """
#         Tests the output of the errors functions
#         """
#         with api_to_test.app.app_context():
#             for key, content in HTTP_STATUS_CODES.items():
#                 response = error_response(key)
#                 print(repr(response))
#                 self.assertEqual(json.dumps(response.status_code), f'{key}')

#     def test_values(self):
#         """
#         Test the input values of the errors functions
#         """
#         pass

#     def test_types(self):
#         pass


class TestApiCalls(TestCase):
    """
    Tests the api.calls module
    """
    def setUp(self):
        """
        Sets up the app and test variables
        """
        api_to_test.app.testing = True
        self.app = api_to_test.app.test_client()

    def test_output(self):
        """
        Tests the output of the API
        """
        good_value_pairs = INT_VALUE_PAIRS
        for pair in good_value_pairs:
            response_value = self.app.get(f'/{pair[0]}')
            data = json.loads(response_value.data)
            self.assertEqual(data['extenso'], f'{pair[1]}')

    def test_values(self):
        """
        Tests the API for bad values
        """
        bad_values = BAD_VALUES_INT
        for value in bad_values:
            response_value = self.app.get(f'/{value}')
            status_code = response_value.status_code
            self.assertEqual(status_code, 400)

    def test_types(self):
        """
        Tests the API for bad types
        """
        bad_types = BAD_TYPES_NO_INT
        for bad_type in bad_types:
            response_value = self.app.get(f'/{bad_type}')
            status_code = response_value.status_code
            self.assertEqual(status_code, 404)
