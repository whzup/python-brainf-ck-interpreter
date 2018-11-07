"""
Constant definitions for the language
"""
# Token type definitions
L_SHIFT, R_SHIFT = 'L_SHIFT', 'R_SHIFT'
INC, DEC = 'INC', 'DEC'
PUT, GET = 'PUT', 'GET'
L_PAREN, R_PAREN = 'L_PAREN', 'R_PAREN'
EOF, EOF_VALUE = 'EOF', chr(4)
INV = 'INV'

# Token value definitions
L_SHIFT_VALUE, R_SHIFT_VALUE = '<', '>'
INC_VALUE, DEC_VALUE = '+', '-'
PUT_VALUE, GET_VALUE = '.', ','
L_PAREN_VALUE, R_PAREN_VALUE = '[', ']'

# All operation symbols
OPERATIONS = ['<', '>', '+', '-', '.', ',']
