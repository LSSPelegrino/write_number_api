"""
Functions to translate an int number to the corresponding cardinal numerals
in portuguese.
Accepts ranges from -99 999 to 99 999.
"""

SUFIXES = (
    '',
    'mil'
)

ONES = (
    '',
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove"
)

AFTER_TEN = (
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove"
)

TENS = (
    '',
    '',
    "vinte",
    "trinta",
    "quarenta",
    "cinquenta",
    "sessenta",
    "setenta",
    "oitenta",
    "noventa",
)

HUNDREDS = (
    '',
    'cento',
    'duzentos',
    'trezentos',
    'quatrocentos',
    'quinhentos',
    'seiscentos',
    'setecentos',
    'oitocentos',
    'novecentos'
)

CARDINAL_MATRIX = (
    ONES,
    AFTER_TEN,
    TENS,
    HUNDREDS
)


def to_cardinal_trio(trio: str):
    """
    Translates a number of no more than 3 digits into its cardinal
    representation.
    The number must be passed as a string in numeric form
    """

    if not isinstance(trio, str):
        raise TypeError("The number must be passed as a string")

    try:
        int(trio)
    except ValueError:
        raise ValueError("The value does not represent an integer")

    digits = 3
    if len(trio) > digits:
        raise ValueError(f"The number value must have {digits} digits or less")

    trio = trio.zfill(digits)

    if trio == '100':
        cardinal_trio = 'cem'
    elif trio == '000':
        cardinal_trio = 'zero'
    else:
        cardinal_trio = ''
        hundreds = int(trio[0])
        tens = int(trio[1])
        units = int(trio[2])

        if hundreds != 0:
            cardinal_trio = CARDINAL_MATRIX[3][hundreds]
        if tens == 1:
            cardinal_trio = cardinal_trio + ' ' \
                + CARDINAL_MATRIX[1][units]
        else:
            if tens != 0:
                cardinal_trio = cardinal_trio + ' ' \
                    + CARDINAL_MATRIX[2][tens]
            if units != 0:
                cardinal_trio = cardinal_trio + ' ' \
                    + CARDINAL_MATRIX[0][units]

    cardinal_trio = cardinal_trio.strip().replace(' ', ' e ')

    return cardinal_trio


def to_cardinal_number(number: int):
    """
    Translate an integer number to portuguese.
    Accepts ranges from -99 999 to 99 999
    """
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("The number must be passed as a integer")

    if abs(number) > 99999:
        raise ValueError("The input value must be between -99999 and 99999")

    sign = 'menos' if number < 0 else ''

    cardinal_number = ''
    max_index = (len(f"{abs(number)}")-1)//3
    number_str = f"{abs(number)}"

    for i in range(0, max_index+1):
        slice_start = -3*(1+i)
        slice_stop = -3*i if i != 0 else None
        trio = number_str[slice_start:slice_stop]
        # trio_int = int(trio)
        if trio == '1' and i == 1:
            cardinal_number = SUFIXES[i] + '_' + cardinal_number
        elif trio != '000':
            cardinal_number = to_cardinal_trio(trio) + ' ' \
                + SUFIXES[i] + '_' \
                + cardinal_number

    cardinal_number = cardinal_number.strip('_ ').replace('_', ' e ')

    return (sign + ' ' + cardinal_number).strip()
