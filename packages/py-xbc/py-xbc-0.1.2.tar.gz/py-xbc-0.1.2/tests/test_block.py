
'''
Test output for XBC blocks.
'''

import pytest

from xbc import loads_xbc, ParseError

def test_empty():
    'An empty block should cause the key to exist.'
    assert loads_xbc('a {}') == {'a': True}

def test_keyvalue():
    'A block should support key/value pairs.'
    assert loads_xbc('a { a = 1 }') == {'a': False, 'a.a': '1'}

def test_nested_block():
    'A block should support having block members.'
    assert loads_xbc('a { b { c = 1 } }') == {'a.b.c': '1', 'a': False, 'a.b': False}

def test_keyvalue_and_block():
    'A key/value pair can be provided for a block key prior to the block.'
    assert loads_xbc('a = 1\na { a = 1 }') == {'a': '1', 'a.a': '1'}

def test_reassign_colon():
    'Attempting to assign to the same key should be an error inside a block too.'
    with pytest.raises(ParseError):
        loads_xbc('a { a = 1; a = 2 }')

def test_assign_after_block():
    'It is an error to assign to a block key after the block.'
    with pytest.raises(ParseError):
        loads_xbc('a { a = 1 }\na = 1')

def test_append_after_block():
    'Modifying keys after a block is legal.'
    loads_xbc('a\na { b = 1 }\na += 1') == {'a': '1', 'a.b': '1'}
