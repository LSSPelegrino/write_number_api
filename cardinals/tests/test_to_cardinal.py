"""
Test cases to the 'to_cardinal' module
"""
# # Standard Modules
import unittest

# # Internal Modules
from cardinals import to_cardinal_number
from cardinals.to_cardinal import to_cardinal_trio


class TestToCardinalTrio(unittest.TestCase):
    """
    Tests the function to_cardinal_trio
    """
    def setUp(self):
        """
        Sets up the good and bad values used to test the function
        """
        self.good_value_pairs = (
            ('0', 'zero'),
            ('1', 'um'),
            ('2', 'dois'),
            ('3', 'três'),
            ('4', 'quatro'),
            ('5', 'cinco'),
            ('6', 'seis'),
            ('7', 'sete'),
            ('8', 'oito'),
            ('9', 'nove'),
            ('10', 'dez'),
            ('11', 'onze'),
            ('12', 'doze'),
            ('13', 'treze'),
            ('14', 'quatorze'),
            ('15', 'quinze'),
            ('16', 'dezesseis'),
            ('17', 'dezessete'),
            ('18', 'dezoito'),
            ('19', 'dezenove'),
            ('20', 'vinte'),
            ('21', 'vinte e um'),
            ('22', 'vinte e dois'),
            ('23', 'vinte e três'),
            ('24', 'vinte e quatro'),
            ('25', 'vinte e cinco'),
            ('26', 'vinte e seis'),
            ('27', 'vinte e sete'),
            ('28', 'vinte e oito'),
            ('29', 'vinte e nove'),
            ('30', 'trinta'),
            ('40', 'quarenta'),
            ('50', 'cinquenta'),
            ('60', 'sessenta'),
            ('70', 'setenta'),
            ('80', 'oitenta'),
            ('90', 'noventa'),
            ('99', 'noventa e nove'),
            ('100', 'cem'),
            ('101', 'cento e um'),
            ('111', 'cento e onze'),
            ('120', 'cento e vinte'),
            ('130', 'cento e trinta'),
            ('140', 'cento e quarenta'),
            ('150', 'cento e cinquenta'),
            ('200', 'duzentos'),
            ('300', 'trezentos'),
            ('400', 'quatrocentos'),
            ('500', 'quinhentos'),
            ('600', 'seiscentos'),
            ('700', 'setecentos'),
            ('800', 'oitocentos'),
            ('900', 'novecentos'),
            ('999', 'novecentos e noventa e nove')
        )

        self.bad_values = ('noventa e nove',
                           '9999',
                           '99999',
                           '999999',)
        self.bad_types = (
            101,
            [1, 0, 1],
            101.0,
            None,
            True)

    def test_output(self):
        """
        Tests the output of the function
        """
        for pair in self.good_value_pairs:
            self.assertEqual(to_cardinal_trio(pair[0]), pair[1])

    def test_values(self):
        """
        Test bad values
        """
        for value in self.bad_values:
            with self.assertRaises(ValueError):
                to_cardinal_trio(value)

    def test_types(self):
        """
        Test bad types
        """
        for value in self.bad_types:
            with self.assertRaises(TypeError):
                to_cardinal_trio(value)


class TestToCardinalNumber(unittest.TestCase):
    """
    Test the function to_cardinal_number
    """
    def setUp(self):
        """
        Sets up the good and bad values used to test the function
        """
        self.good_value_pairs = (
            (0, 'zero'),
            (1, 'um'),
            (2, 'dois'),
            (3, 'três'),
            (4, 'quatro'),
            (5, 'cinco'),
            (6, 'seis'),
            (7, 'sete'),
            (8, 'oito'),
            (9, 'nove'),
            (10, 'dez'),
            (11, 'onze'),
            (12, 'doze'),
            (13, 'treze'),
            (14, 'quatorze'),
            (15, 'quinze'),
            (16, 'dezesseis'),
            (17, 'dezessete'),
            (18, 'dezoito'),
            (19, 'dezenove'),
            (20, 'vinte'),
            (30, 'trinta'),
            (40, 'quarenta'),
            (50, 'cinquenta'),
            (60, 'sessenta'),
            (70, 'setenta'),
            (80, 'oitenta'),
            (90, 'noventa'),
            (100, 'cem'),
            (101, 'cento e um'),
            (111, 'cento e onze'),
            (120, 'cento e vinte'),
            (150, 'cento e cinquenta'),
            (170, 'cento e setenta'),
            (200, 'duzentos'),
            (300, 'trezentos'),
            (400, 'quatrocentos'),
            (500, 'quinhentos'),
            (600, 'seiscentos'),
            (700, 'setecentos'),
            (800, 'oitocentos'),
            (900, 'novecentos'),
            (999, 'novecentos e noventa e nove'),
            (1000, 'mil'),
            (2000, 'dois mil'),
            (3000, 'três mil'),
            (4000, 'quatro mil'),
            (5000, 'cinco mil'),
            (6000, 'seis mil'),
            (7000, 'sete mil'),
            (8000, 'oito mil'),
            (9000, 'nove mil'),
            (9999, 'nove mil e novecentos e noventa e nove'),
            (10000, 'dez mil'),
            (11000, 'onze mil'),
            (20000, 'vinte mil'),
            (50000, 'cinquenta mil'),
            (90000, 'noventa mil'),
            (99000, 'noventa e nove mil'),
            (99900, 'noventa e nove mil e novecentos'),
            (99990, 'noventa e nove mil e novecentos e noventa'),
            (99999, 'noventa e nove mil e novecentos e noventa e nove'),
            (-1, 'menos um'),
            (-2, 'menos dois'),
            (-3, 'menos três'),
            (-4, 'menos quatro'),
            (-5, 'menos cinco'),
            (-6, 'menos seis'),
            (-7, 'menos sete'),
            (-8, 'menos oito'),
            (-9, 'menos nove'),
            (-10, 'menos dez'),
            (-11, 'menos onze'),
            (-12, 'menos doze'),
            (-13, 'menos treze'),
            (-14, 'menos quatorze'),
            (-15, 'menos quinze'),
            (-16, 'menos dezesseis'),
            (-17, 'menos dezessete'),
            (-18, 'menos dezoito'),
            (-19, 'menos dezenove'),
            (-20, 'menos vinte'),
            (-30, 'menos trinta'),
            (-40, 'menos quarenta'),
            (-50, 'menos cinquenta'),
            (-60, 'menos sessenta'),
            (-70, 'menos setenta'),
            (-80, 'menos oitenta'),
            (-90, 'menos noventa'),
            (-100, 'menos cem'),
            (-101, 'menos cento e um'),
            (-111, 'menos cento e onze'),
            (-120, 'menos cento e vinte'),
            (-150, 'menos cento e cinquenta'),
            (-170, 'menos cento e setenta'),
            (-200, 'menos duzentos'),
            (-300, 'menos trezentos'),
            (-400, 'menos quatrocentos'),
            (-500, 'menos quinhentos'),
            (-600, 'menos seiscentos'),
            (-700, 'menos setecentos'),
            (-800, 'menos oitocentos'),
            (-900, 'menos novecentos'),
            (-999, 'menos novecentos e noventa e nove'),
            (-1000, 'menos mil'),
            (-2000, 'menos dois mil'),
            (-3000, 'menos três mil'),
            (-4000, 'menos quatro mil'),
            (-5000, 'menos cinco mil'),
            (-6000, 'menos seis mil'),
            (-7000, 'menos sete mil'),
            (-8000, 'menos oito mil'),
            (-9000, 'menos nove mil'),
            (-9999, 'menos nove mil e novecentos e noventa e nove'),
            (-10000, 'menos dez mil'),
            (-11000, 'menos onze mil'),
            (-20000, 'menos vinte mil'),
            (-50000, 'menos cinquenta mil'),
            (-90000, 'menos noventa mil'),
            (-99000, 'menos noventa e nove mil'),
            (-99900, 'menos noventa e nove mil e novecentos'),
            (-99990, 'menos noventa e nove mil e novecentos e noventa'),
            (-99999, 'menos noventa e nove mil e novecentos e noventa e nove')
        )

        self.bad_values = (100000,
                           123456)

        self.bad_types = (
            "onze mil cento e um",
            [1, 1, 1, 0, 1],
            11101.0,
            None,
            True)

    def test_output(self):
        """
        Tests the output of the function
        """
        for pair in self.good_value_pairs:
            self.assertEqual(to_cardinal_number(pair[0]), pair[1])

    def test_values(self):
        """
        Test bad values
        """
        for value in self.bad_values:
            with self.assertRaises(ValueError):
                to_cardinal_number(value)

    def test_types(self):
        """
        Test bad types
        """
        for value in self.bad_types:
            with self.assertRaises(TypeError):
                to_cardinal_number(value)
