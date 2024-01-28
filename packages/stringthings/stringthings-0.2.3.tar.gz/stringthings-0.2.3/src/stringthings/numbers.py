# -*-coding: utf-8 -*-
"""
Created on Mon Jan 01 13:53:33 2024

@author: Martín Araya
"""

__all__ = ['is_numeric', 'get_number']


def is_numeric(string):
    """
    returns True if the string is a number
    """
    if 'j' in string.lower():
        try:
            complex(string)
            return True
        except:
            return False
    else:
        string = string.strip('() +-').replace("'", '').replace(' ', '').replace(',', '.')
        try:
            float(string)
            return True
        except:
            return False


def get_number(string):
    """
    returns the number, as integer, float or complex, contained in a numeric string
    """
    if is_numeric(string):
        string = string.lower()
        if 'j' in string:
            return complex(string)
        else:
            string = string.replace(' ', '').replace("'", '').replace(',', '.').strip('+')
            if string.endswith('-'):
                string = '-' + string.strip('-')
            if string.startswith('(') and string.endswith(')'):
                string = '-' + string.strip('-()')
            if '.' in string:
                if 'e' in string and '.' in string.split('e')[-1]:
                    return float(string.slit('e')[0]) * 10 ** float(string.split('e')[-1])
                else:
                    return float(string)
            elif 'e' in string:
                return int(string.split('e')[0]) * 10 ** int(string.split('e')[-1])
            else:
                return int(string)
    else:
        raise ValueError(f"{string} doesn't represent a number.")
