"""
A LL(1) recursive descent parser which parses
the code into a homogeneous AST.
"""
from ast import *


class Parser:
    """LL(1) recursive descent parser"""
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.lexer.tokenize()
        self.token_list = self.lexer.token_list
        self.parse_pos = 0
        self.lookahead = self.token_list[self.parse_pos]
        self.loop_flag = False
        self.ast = AST(token_type='ROOT')
        self.current_node = self.ast

    def consume(self):
        """Consumes the current token"""
        self.parse_pos += 1
        self.lookahead = self.lexer.token_list[self.parse_pos]

    def match(self, exp):
        """Matches the lookahead to a specified value exp"""
        if self.lookahead.value == EOF_VALUE:
            # print("Matched EOF")
            return 0
        elif self.lookahead.value == exp:
            self.consume()
            # print("Matched {}".format(exp))
        else:
            raise Exception("Expected {}, found {}".format(exp, self.lookahead.value))

    def loop(self):
        """Rules for a loop"""
        self.match(L_PAREN_VALUE)
        self.loop_flag = True
        self.operations()
        self.loop_flag = False
        self.current_node.add_child(AST(token=self.lookahead))
        self.match(R_PAREN_VALUE)

    def operations(self):
        """Rules for operations"""
        self.operation()
        while self.lookahead.value != EOF_VALUE:
            if self.lookahead.value == R_PAREN_VALUE:
                break
            self.operation()

    def operation(self):
        """Rules for one operation"""
        if self.lookahead.value in OPERATIONS:
            self.current_node.add_child(AST(token=self.lookahead))
            if not self.loop_flag:
                self.current_node = self.current_node.children[-1]
            self.match(self.lookahead.value)
        elif self.lookahead.value == L_PAREN_VALUE:
            self.current_node.add_child(AST(token=self.lookahead))
            self.current_node = self.current_node.children[-1]
            self.loop()
        elif self.lookahead.value == EOF_VALUE:
            self.eof()
        else:
            raise Exception("Expected operation or loop start, found {}".format(self.lookahead.value))

    def eof(self):
        """Rule for EOF"""
        self.match(EOF_VALUE)
