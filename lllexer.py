"""
A LL(1) recursive descent lexer and the Token class
used to tokenize the input.
"""
from language import *
import logging


class Token:
    """Defines a basic token with a value and a type"""
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.token_type,
            value=repr(self.value)
        )


class Lexer:
    """LL(1) recursive descent lexer"""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.token_list = []
        self.logger = logging.getLogger(__name__)

    def consume(self):
        """
        Consume a character if it is inside the range of the text
        else set the current character to EOF.
        """
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = EOF

    def next_token(self):
        """Returns the Token of the next character"""
        while self.current_char != EOF:
            if self.current_char == L_SHIFT_VALUE:
                self.consume()
                return Token(L_SHIFT, L_SHIFT_VALUE)
            elif self.current_char == R_SHIFT_VALUE:
                self.consume()
                return Token(R_SHIFT, R_SHIFT_VALUE)
            elif self.current_char == INC_VALUE:
                self.consume()
                return Token(INC, INC_VALUE)
            elif self.current_char == DEC_VALUE:
                self.consume()
                return Token(DEC, DEC_VALUE)
            elif self.current_char == PUT_VALUE:
                self.consume()
                return Token(PUT, PUT_VALUE)
            elif self.current_char == GET_VALUE:
                self.consume()
                return Token(GET, GET_VALUE)
            elif self.current_char == L_PAREN_VALUE:
                self.consume()
                return Token(L_PAREN, L_PAREN_VALUE)
            elif self.current_char == R_PAREN_VALUE:
                self.consume()
                return Token(R_PAREN, R_PAREN_VALUE)
            else:
                self.consume()
        return Token(EOF, EOF_VALUE)

    def tokenize(self):
        """Tokenize the whole text"""
        token = self.next_token()
        while token.token_type != EOF:
            self.token_list.append(token)
            self.logger.debug("New token {}".format(token))
            # yield token
            token = self.next_token()
        self.token_list.append(token)
        # yield token
