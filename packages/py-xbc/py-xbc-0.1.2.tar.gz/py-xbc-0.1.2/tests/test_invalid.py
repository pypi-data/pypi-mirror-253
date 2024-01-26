
'''
Tests for inputs which are invalid.
'''

import pytest

from pyparsing.exceptions import ParseException
from xbc import loads_xbc, ParseError

# this should fail but does not.
@pytest.mark.xfail
def test_whitespace_vc():
    'Whitespace is prohibited between values and commas.'
    with pytest.raises(ParseError):
        loads_xbc('x = a\n, b')

# this should fail but does not.
@pytest.mark.xfail
def test_extra_quote():
    'Strings cannot contain the quote style that bookends them.'
    with pytest.raises(ParseException):
        loads_xbc("x = '''")

def test_lone_plus():
    'Bare operators are not permitted.'
    with pytest.raises(ParseException):
        loads_xbc('+')

def test_lone_rbrace():
    'Braces can only appear as part of a block.'
    with pytest.raises(ParseException):
        loads_xbc('}')

def test_lone_lbrace():
    'Braces can only appear as part of a block.'
    with pytest.raises(ParseException):
        loads_xbc('{')

def test_lone_braces():
    'Braces can only appear as part of a block.'
    with pytest.raises(ParseException):
        loads_xbc('{}')

def test_lone_semi():
    'Semicolons are only permitted as part of a key or key/value statement.'
    with pytest.raises(ParseException):
        loads_xbc(';')

def test_empty():
    'XBC files cannot be empty.'
    with pytest.raises(ParseException):
        loads_xbc('\n')
    with pytest.raises(ParseException):
        loads_xbc('')
