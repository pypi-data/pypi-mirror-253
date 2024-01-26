# py-xbc

`py-xbc` is a pure-Python library for reading and writing files in the
eXtra BootConfig (XBC) file format specified by the Linux kernel. This
is not a strictly-conforming implementation: in particular, this
implementation does not enforce the 32,767-byte ceiling on XBC files,
nor does it enforce the 16-level cap on keys and blocks.

# Requirements

`py-xbc` currently requires `pyparsing` and Python 3.7+.

# Usage

`py-xbc` exports four functions:

- `loads_xbc` parses a string.
- `load_xbc` opens a file and then parses a string.
- `saves_xbc` renders to a string.
- `save_xbc` renders to a string and writes the string to a file.

## Format

XBC files consist of a series of statements, of which there are three
kinds:

- A key is a sequence of one or more bytes in the range `a-zA-Z0-9_-`.
  They are namespaced with periods (`.`) and may be followed by an
  equals sign (`=`). Key statements are terminated by a semicolon (`;`),
  a linefeed, or a semicolon followed by a linefeed.

- A key/value statement is a key followed by an operator, followed in
  turn by one or more values. There are three operators:

  - Assignment (`=`) specifies an initial value.
  - Updates (`:=`) overwrites whatever value was previously there.
  - Appends (`+=`) appends one or more values.

  There are two kinds of values: strings and arrays. Strings can be
  either 'bare' or quoted.

  - Bare strings are a sequence of one or more bytes that are not in the
    range `{}#=+:;,\n'" `.
  - Quoted strings are a sequence of bytes that begins with a single
    quote (`'`) or a double quote (`"`) and ends only with the same
    quote. Quotes cannot be escaped.
  - Arrays are a sequence of one or more values delimited by a comma
    (`,`).

- A block is a key followed by a pair of curly braces, inside which is
  one or more key or key/value statements.

Keys are composable. The following examples are equivalent:

```xbc
foo {
    bar {
        fluff = 1
    }
}
# is equivalent to
foo.bar.fluff = 1
# is equivalent to
foo.bar { fluff = 1 }
# is equivalent to
foo { bar.fluff = 1 }
```

# Licence

`py-xbc` is published under the MIT license. See `LICENSE.txt` for more
information.
