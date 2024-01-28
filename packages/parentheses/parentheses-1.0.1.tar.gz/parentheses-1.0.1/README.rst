Parentheses. V1.0.0
===================

Light parentheses parser in Python.

Types (Aliases)
----------------

.. code-block:: python

    ParenthesesSymbol = str
    ParseFlag = int

Constants
---------

.. code-block:: python

    PARENTHESES_ALL: ParseFlag = 1
    PARENTHESES_OPEN: ParseFlag = 2
    PARENTHESES_CLOSE: ParseFlag = 3

    PARENTHESES_ROUND_OPEN: ParenthesesSymbol = '('
    PARENTHESES_ROUND_CLOSE: ParenthesesSymbol = ')'

    PARENTHESES_SQUARE_OPEN: ParenthesesSymbol = '['
    PARENTHESES_SQUARE_CLOSE: ParenthesesSymbol = ']'

    PARENTHESES_CURLY_OPEN: ParenthesesSymbol = '{'
    PARENTHESES_CURLY_CLOSE: ParenthesesSymbol = '}'

    PARENTHESES_DOUBLE_QUOTE: ParenthesesSymbol = '"'

    PARENTHESES_SINGLE_QUOTE: ParenthesesSymbol = '\''

    PARENTHESES_OPEN_SYMBOLS: list[ParenthesesSymbol] = [
        PARENTHESES_ROUND_OPEN,
        PARENTHESES_SQUARE_OPEN,
        PARENTHESES_CURLY_OPEN
    ]

    PARENTHESES_CLOSE_SYMBOLS: list[ParenthesesSymbol] = [
        PARENTHESES_ROUND_CLOSE,
        PARENTHESES_SQUARE_CLOSE,
        PARENTHESES_CURLY_CLOSE
    ]

    PARENTHESES_SYMBOLS = PARENTHESES_OPEN_SYMBOLS + PARENTHESES_CLOSE_SYMBOLS

    PARENTHESES_REGEX = r'\(.*?\)|\[.*?\]|\{.*?\}'

``PPString`` class
--------------------

``PPString`` is a class that represents a parsed parentheses string.

``valid_proc() -> bool``
~~~~~~~~~~~~~~~~~~~~~~~~

Get is parentheses in string valid. (Slower but gives more accurate result).

Examples:

- ``parse('(x)').valid_proc()`` => ``True``
- ``parse('(x').valid_proc()`` => ``False``

``valid() -> bool``
~~~~~~~~~~~~~~~~~~~

Get is parentheses in string valid. (Faster but gives less accurate result).

Examples:

- ``parse('(x)').valid()`` => ``True``
- ``parse('(x').valid()`` => ``False``

``valid_quotes(_escaping: bool=False) -> bool``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get is quoted parentheses valid.

Examples:

- ``parse('"x"').valid_quotes()`` => ``True``
- ``parse('"x\""').valid_quotes(True)`` => ``True``
- ``parse('"x').valid_quotes()`` => ``False``
- ``parse('"x\""').valid_quotes()`` => ``False``

``count(flag: ParseFlag=PARENTHESES_ALL) -> int``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Count braces in string.

Examples:

- ``parse('(x)').count()`` => ``2``
- ``parse('(x)').count(PARENTHESES_OPEN)`` => ``1``
- ``parse('(x)').count(PARENTHESES_CLOSE)`` => ``1``

``autoclose() -> str``
~~~~~~~~~~~~~~~~~~~~~~

Autoclose brackets.

Examples:

- ``parse('{[(x').autoclose()`` => ``{[(x)]}``

``find(remove_braces: bool=False) -> list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get content in braces.

Examples:

- ``parse('(x) [y] {z}').find()`` => ``['(x)', '[y]', '{z}']``
- ``parse('(x) [y] {z}').find(True)`` => ``['x', 'y', 'z']``

``remove_braces() -> str``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove braces in string.

Examples:

- ``parse('(x) [y] {z}').remove_braces()`` => ``'x y z'``

``remove(keep_braces: bool=False) -> str``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove everything in parentheses.

Examples:

- ``parse('(x) [y] {z}').remove()`` => ``'   '``
- ``parse('(x) [y] {z}').remove(True)`` => ``'() [] {}'``

``as_str() -> str``
~~~~~~~~~~~~~~~~~~~

Get string.

Examples:

- ``parse('x').as_str()`` => ``'x'``

Global functions
------------------

``parse(string: str) -> PPString``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parse string.

Examples:

- ``parse('(x)')`` => ``PPString('x')``

``new_parentheses_symbols(open_symbol: ParenthesesSymbol, close_symbol: ParenthesesSymbol) -> None``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add new parentheses symbols.

Examples:

- ``new_parentheses_symbols('<', '>')`` => ``None``

``remove_parentheses_symbols(open_symbol: ParenthesesSymbol, close_symbol: ParenthesesSymbol) -> None``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove parentheses symbols.

Examples:

- ``remove_parentheses_symbols('<', '>')`` => ``None``
