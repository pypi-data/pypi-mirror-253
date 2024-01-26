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
Utility functions for saving data in XBC format.
'''

import re

from collections.abc import Sequence, Mapping

KEY_RE   = re.compile(r'^[a-zA-Z0-9_-]+(?:\.(?:[a-zA-Z0-9_-]+))*$')
NVAL_RE  = re.compile(r'^[^{}=+:;,\n\'"]+$')
QUOTES   = '\'"'
QUOTEMAP = {'"': "'", "'": '"'}
ESCAPES  = {
    'backslash': {'"': '\\x22', "'": '\\x27'},
    'html': {'"': '&quot;', "'": '&apos;'},
    'url': {'"': '%22', "'": '%27'}
}

def quote(data, escape='backslash'):
    'Quote data according to XBC rules.'
    # don't waste our time if it's a valid bare value.
    if NVAL_RE.match(data) is not None:
        return data
    esc = None

    # how shall we escape embedded quotes?
    if isinstance(esc, Mapping):
        if '"' in escape and "'" in escape:
            esc = escape
    else:
        esc = ESCAPES.get(escape, None)

    if esc is None:
        raise ValueError('unrecognised escape format')

    f = data[0]

    # is this a quoted string?
    if f in QUOTES and data[-1] == f:
        # return it if we don't need to do anything
        if f not in data[1:-1]:
            return data
        # escape embedded quotes
        x = data[1:-1].replace(f, esc[f])
        return f'{f}{x}{f}'

    # if the other quote isn't used, wrap in it
    if f in QUOTES and QUOTEMAP[f] not in data[1:]:
        q = QUOTEMAP[f]
    # not a quoted string, but has only one kind of quote
    elif "'" in data and '"' not in data:
        q = '"'
    elif '"' in data and "'" not in data:
        q = "'"
    else:
        # not a quoted string and has both types; we escape one
        data = data.replace("'", esc["'"])
        q = "'"
    return f'{q}{data}{q}'

def normalise_string(string):
    'Normalise values according to XBC rules.'
    if not isinstance(string, str):
        string = str(string)

    if NVAL_RE.match(string) is None:
        string = quote(string)

    return string

def normalise(data):
    '''Normalise values according to XBC rules.'''
    if isinstance(data, str) or not isinstance(data, (Sequence, Mapping)):
        return normalise_string(data)

    if isinstance(data, Sequence):
        ret = []

        for item in data:
            if isinstance(item, str) or not isinstance(item, (Sequence, Mapping)):
                ret.append(normalise_string(item))
            # we can unwind nested sequences
            elif isinstance(item, Sequence):
                ret.extend(normalise(item))
            # ...but we can't do that with mappings, the format doesn't
            # support it.
            elif isinstance(item, Mapping):
                raise ValueError('nested mapping')
            else:
                # this should be impossible to reach, but nothing truly is.
                raise ValueError(type(item))

        ret = ', '.join(ret)

        return ret

    if isinstance(data, Mapping):
        d = {}
        for k, v in data.items():
            if KEY_RE.match(k) is None:
                raise KeyError(k)

            v = normalise(v)

            d[k] = v

        return d

    return data

__all__ = ['quote', 'normalise', 'normalise_string']
