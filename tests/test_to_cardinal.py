"""
Test cases to the 'to_cardinal' module.
Call these tests on the command line at project root using:
    $ python -m unittest tests.test_to_cardinal
"""
# # Standard Modules
from unittest import TestCase

# # Internal Modules
from cardinals import to_cardinal_number
from cardinals.to_cardinal import to_cardinal_trio
from .test_variables import STR_VALUE_PAIRS
from .test_variables import INT_VALUE_PAIRS
from .test_variables import BAD_VALUES_STR
from .test_variables import BAD_VALUES_INT
from .test_variables import BAD_TYPES_NO_STR
from .test_variables import BAD_TYPES_NO_INT


class TestToCardinalTrio(TestCase):
    """
    Tests the function to_cardinal_trio
    """
    def test_output(self):
        """
        Tests the output of the function
        """
        good_value_pairs = STR_VALUE_PAIRS
        for pair in good_value_pairs:
            output = to_cardinal_trio(pair[0])
            self.assertEqual(output, pair[1],
                             f"{pair[0]} should be {pair[1]}, not {output}")

    def test_values(self):
        """
        Test bad values
        """
        bad_values = BAD_VALUES_STR
        for value in bad_values:
            with self.assertRaises(ValueError):
                to_cardinal_trio(value)

    def test_types(self):
        """
        Test bad types
        """
        bad_types = BAD_TYPES_NO_STR
        for value in bad_types:
            with self.assertRaises(TypeError):
                to_cardinal_trio(value)


class TestToCardinalNumber(TestCase):
    """
    Test the function to_cardinal_number
    """

    def test_output(self):
        """
        Tests the output of the function
        """
        good_value_pairs = INT_VALUE_PAIRS
        for pair in good_value_pairs:
            output = to_cardinal_number(pair[0])
            self.assertEqual(output, pair[1],
                             f"{pair[0]} should be {pair[1]}, not {output}")

    def test_values(self):
        """
        Test bad values
        """
        bad_values = BAD_VALUES_INT
        for value in bad_values:
            with self.assertRaises(ValueError):
                to_cardinal_number(value)

    def test_types(self):
        """
        Test bad types
        """
        bad_types = BAD_TYPES_NO_INT
        for value in bad_types:
            with self.assertRaises(TypeError):
                to_cardinal_number(value)
