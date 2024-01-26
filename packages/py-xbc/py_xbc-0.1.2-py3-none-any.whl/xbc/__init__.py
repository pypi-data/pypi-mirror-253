# Copyright (c) 2024 Síle Ekaterin Liszka
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
This module implements support for the eXtra Boot Configuration file
format specified by the Linux kernel. For more information, please see
https://docs.kernel.org/admin-guide/bootconfig.html for more
information.

This is not a strictly-conforming implementation. In particular, this
module does not adhere to the kernel's 32,767-byte restriction and does
not enforce the maximum depth of 16 namespaces.
'''

import re

from collections.abc import Mapping, Sequence

from pyparsing import (
    alphas,
    CharsNotIn,
    DelimitedList,
    Forward,
    Group,
    nums,
    Literal,
    OneOrMore,
    Optional,
    Regex,
    restOfLine,
    QuotedString,
    Word,
    ZeroOrMore
)

from .utils import normalise
from .version import version as __version__

class XBCNode:
    # pylint: disable=too-few-public-methods
    'An XBC XBCNode.'
    def __init__(self, *args, kind=None):
        if isinstance(args[0], str):
            self.args = args[0]
        elif isinstance(args[0][0], str):
            self.args = args[0][0]
        else:
            self.args = args[0][0][0]
        self.type = kind

    @property
    def key(self):
        'The key associated with the node.'
        return self.args[0]

class XBCKey(XBCNode):
    # pylint: disable=too-few-public-methods
    'An XBC key.'
    def __init__(self, *args):
        # pylint: disable=super-init-not-called
        self.args = args[0]
        self.type = 'key'

class XBCKeyValue(XBCNode):
    'An XBC key/value operation.'
    def __init__(self, *args):
        super().__init__(args, kind='kv')

    @property
    def op(self):
        'The operator being performed.'
        return self.args[1]

    @property
    def value(self):
        'The data associated with the operation.'
        return self.args[2]

class XBCBlock(XBCNode):
    'An XBC block.'
    def __init__(self, *args):
        super().__init__(args, kind='block')

    @property
    def contents(self):
        'The contents of the block.'
        return self.args[1]

XBCParser = None

class ParseError(Exception):
    'Exception for parsing errors.'

def lex(data):
    # pylint: disable=too-many-locals,global-statement,unnecessary-lambda
    'Run the lexer over the provided data.'
    global XBCParser

    if XBCParser is None:
        key_fragment = Word(alphas + nums + '_-')
        key = DelimitedList(key_fragment, delim='.', combine=True)

        bareval = CharsNotIn('{}#=+:;,\n\'"')
        strvals = QuotedString("'", multiline=True, unquote_results=False)
        strvald = QuotedString('"', multiline=True, unquote_results=False)
        value = bareval | strvald | strvals

        assign = Literal('=')
        update = Literal(':=')
        append = Literal('+=')
        op = assign | update | append
        lbrace = Literal('{').suppress()
        rbrace = Literal('}').suppress()
        terminal = Word(';\n').suppress()

        NL = Literal('\n').suppress()     # pylint: disable=invalid-name
        WS = Word(' \t').suppress()       # pylint: disable=invalid-name
        WS_NL = Word(' \t\n').suppress()  # pylint: disable=invalid-name
        comment = Literal('#') + restOfLine

        values = Group(
            value + ZeroOrMore(
                Literal(',').suppress() +
                Optional(WS_NL) + value
            ), aslist=True
        )

        keyvalue = Group(key + Optional(WS) + op + Optional(WS) + values, aslist=True)
        keyvalue.set_parse_action(lambda x: XBCKeyValue(x))

        key_stmt = key + Optional(WS) + Optional(assign).suppress() + Optional(WS)
        key_stmt.set_parse_action(lambda x: XBCKey(x))

        block = Forward()
        statement = keyvalue | key_stmt
        statements = DelimitedList(statement, delim=terminal)
        segment = Group(OneOrMore(block | statements), aslist=True)

        # pylint: disable=expression-not-assigned
        block << Group(key + Optional(WS) + lbrace + segment + rbrace + Optional(NL))
        block.set_parse_action(lambda x: XBCBlock(x))

        XBCParser = OneOrMore(segment)

        XBCParser.ignore(comment)

    # pylint: disable=too-many-function-args
    return XBCParser.parseString(data).asList()

def unquote(val):
    'Remove quotes and trailing whitespace from values.'
    if val[0] in '\'"' and val[0] == val[-1]:
        return val[1:-1]
    return val.strip()

def key_walk(d, key):
    'Walk the key to guard against post-block key assignments.'
    split = key.split('.')

    for i in range(len(split) - 1, 0, -1):
        x = '.'.join(split[:i])
        if x not in d:
            d[x] = False

def parse_block(key, seq):
    # pylint: disable=too-many-branches,too-many-statements
    'Parse the AST in to a real data structure.'
    if isinstance(seq, list) and len(seq) == 1 and isinstance(seq[0], list):
        seq = seq[0]

    ret = {}

    for item in seq:
        if key is not None:
            k = f'{key}.{item.key}'
        else:
            k = item.key

        if isinstance(item, XBCKey):
            if k not in ret:
                ret[k] = True
                key_walk(ret, k)
            else:
                raise ParseError(f'key {k} already defined')
        elif isinstance(item, XBCKeyValue):
            value = item.value
            op = item.op

            if op == '=':
                if k in ret:
                    raise ParseError(f'key {k} already defined')
                assign = value
            else:
                if k not in ret:
                    raise ParseError(f'key {k} not defined')

                if op == '+=':
                    if isinstance(ret[k], str):
                        assign = [ret[k]]
                    elif ret[k] is True:
                        assign = []
                    else:
                        assign = ret[k]
                    if isinstance(value, str):
                        assign.append(value)
                    else:
                        assign.extend(value)
                    if isinstance(assign, list) and len(assign) == 1:
                        assign = assign[0]
                else:
                    assign = value

            if isinstance(assign, list):
                for i, item in enumerate(assign):
                    assign[i] = unquote(item)
            else:
                assign = unquote(assign)

            if isinstance(assign, list) and len(assign) == 1:
                assign = assign[0]

            ret[k] = assign

            if '.' in k:
                key_walk(ret, k)
        elif isinstance(item, XBCBlock):
            value = item.contents

            if k not in ret:
                ret[k] = False

            if not isinstance(value, list):
                value = [value]

            d = parse_block(k, value)

            for k, v in d.items():
                if k in ret:
                    continue
                ret[k] = v

    return ret

def parse(data):
    'Call the lexer and then the parser.'
    tree = lex(data)

    d = parse_block(None, tree)

    return d

def loads_xbc(data):
    'Load XBC data provided in a string.'
    return parse(data)

def load_xbc(fp):
    'Open a file and parse its contents.'
    with open(fp, mode='r', encoding='UTF-8') as f:
        return loads_xbc(f.read())

def longest_key(seq):
    'Find the deepest-nested key in the sequence provided.'
    lens = [len(x) for x in seq]
    shortest = min(lens)

    if shortest < 1:
        return None

    ret = []

    for i in range(shortest):
        count = {}

        for item in seq:
            j = item[i]

            if j not in count:
                count[j] = 0

            count[j] += 1
        if len(count.keys()) == 1:
            ret.append(seq[0][i])
        else:
            return '.'.join(ret)
    return None

def longest_keys(keys):
    'Find the longest keys in the sequence provided.'
    keys = [k.split('.') for k in keys]
    ret = set()

    for a in keys:
        for b in keys[1:]:
            longest = longest_key([a, b])
            if longest is not None:
                ret.add(longest)
    ret.discard('')
    return ret

def make_block(data):
    # pylint: disable=too-many-locals,too-many-branches
    'Create XBC blocks.'
    ret = []

    leafs = []
    blocks = set()

    for key in data.keys():
        if '.' not in key:
            leafs.append(key)
        else:
            k, _ = key.split('.', maxsplit=1)
            blocks.add(k)

    keys = [k for k in data.keys() if '.' in k]
    temp = longest_keys(keys)
    if temp:
        mindots = 99
        for i in temp:
            if 0 < i.count('.') < mindots:
                mindots = i.count('.')
        temp = [i for i in temp if i.count('.') == mindots]
        blocks = set(temp)

    for key in leafs:
        if data[key] is True:
            ret.append(f'{key}')
        elif data[key] is False:
            continue
        else:
            value = normalise(data[key])
            ret.append(f'{key} = {value}')

    for key in blocks:
        block = {}
        klen = len(key) + 1

        for k, v in data.items():
            if not k.startswith(f'{key}.'):
                continue
            block[k[klen:]] = v

        chunk = make_block(block)
        ret.append(key + ' {')
        for line in chunk:
            ret.append(f'\t{line}')
        ret.append('}')

    return ret

def saves_xbc(data):
    'Export the provided dictionary to an XBC-formatted string.'
    ret = make_block(data)
    return '\n'.join(ret)

def save_xbc(data, filename):
    'Export the provided dictionary to an XBC-formatted string and save it.'
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(saves_xbc(data))

__all__ = ['loads_xbc', 'load_xbc', 'saves_xbc', 'save_xbc', 'ParseError']
