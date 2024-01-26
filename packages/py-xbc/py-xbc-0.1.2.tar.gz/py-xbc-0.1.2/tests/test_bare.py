
'''
Tests for base-level keys.
'''

import pytest

from xbc import loads_xbc, ParseError

def test_key():
    'A key by itself exists.'
    assert loads_xbc('a') == {'a': True}

def test_dot_key():
    'A nested key by itself exists.'
    assert loads_xbc('a.a') == {'a': False, 'a.a': True}

def test_key_eq():
    'A key with an empty assignment exists.'
    assert loads_xbc('a =') == {'a': True}

def test_keyvalue():
    'A bare value can be assigned to a key.'
    assert loads_xbc('a = 1') == {'a': '1'}

def test_keyvalue_space():
    'A bare value can have spaces.'
    assert loads_xbc('a = a b') == {'a': 'a b'}

def test_dot_keyvalue():
    'A key being assigned to can have dots.'
    assert loads_xbc('a.a = 1') == {'a': False, 'a.a': '1'}

def test_keys():
    'Statements can be separated by semicolons.'
    assert loads_xbc('a;b') == {'a': True, 'b': True}

def test_dot_keys():
    'Keys in compound statements can have dots.'
    assert loads_xbc('a.a;a.b') == {'a': False, 'a.a': True, 'a.b': True}

def test_quoted():
    'Values can be quoted with single or double quotes.'
    assert loads_xbc('a = "b"') == {'a': 'b'}

def test_quoted_space():
    'Quoted values can have trailing whitespace preserved.'
    assert loads_xbc('a = "b "') == {'a': 'b '}

def test_array():
    'Multiple values can be assigned to a single key.'
    assert loads_xbc('a = 1, 2') == {'a': ['1', '2']}

def test_reassignment():
    'Keys cannot be reassigned.'
    with pytest.raises(ParseError):
        loads_xbc('a = 1\na = 2')

def test_reassignment_colon():
    'Keys cannot be reassigned, even in compound statements.'
    with pytest.raises(ParseError):
        loads_xbc('a = 1;a = 2')

def test_ovewrite_nonexistent():
    'Keys can only be updated if they exist.'
    with pytest.raises(ParseError):
        loads_xbc('a := 1')

def test_append_key():
    'Append an item to a key.'
    assert loads_xbc('a; a += 1') == {'a': '1'}

def test_append_single():
    'Append an item to a single-item value.'
    assert loads_xbc('a = 1; a += 2') == {'a': ['1', '2']}

def test_append_single2():
    'Append multiple items to a single-item value.'
    assert loads_xbc('a = 1; a += 2, 3') == {'a': ['1', '2', '3']}

def test_append_multi():
    'Append an item to an array value'
    assert loads_xbc('a = 1, 2; a += 3') == {'a': ['1', '2', '3']}

def test_append_multi2():
    'Append multiple items to an array value.'
    assert loads_xbc('a = 1, 2; a += 3, 4') == {'a': ['1', '2', '3', '4']}
