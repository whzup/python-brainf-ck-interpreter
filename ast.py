"""
An abstract syntax tree (AST) which holds only
the necessary information for the interpretation
of the BF code.
"""
from lllexer import *


class AST:
    """Abstract Syntax Tree"""
    def __init__(self, token=None, token_type=None):
        if token is not None:
            self.token = token
        if token_type is not None:
            self.token = Token(token_type, 0)
        self.children = None

    def __str__(self):
        if self.is_nil():
            return "nil"
        else:
            return self.token.token_type

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def is_nil(self):
        return self.token is None

    def str_tree(self):
        """Print the AST using a depth first search"""
        if self.children is None or len(self.children) == 0:
            return self.__str__()
        str_tree = ""
        if not self.is_nil():
            str_tree = "".join([str_tree, "({} ".format(self.__str__())])
        for i in range(len(self.children)):
            subtree = self.children[i]
            if i > 0:
                str_tree = "".join([str_tree, " "])
            str_tree = "".join([str_tree, subtree.str_tree()])
        if not self.is_nil():
            str_tree = "".join([str_tree, ") "])
        return str_tree
