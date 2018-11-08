"""
The interpreter which unites the parser which
creates an AST and the visitor which traverses
the AST and interprets the code.
"""
from llparser import *
from visitor import *
import logging

FORMAT = '%(asctime)-15s - %(levelname)s |  %(message)s  '
logging.basicConfig(format=FORMAT)


class Interpreter:
    """Interpreter class which unites the parser and the visitor"""
    def __init__(self, text):
        self.parser = Parser(text)
        self.ast_visitor = ASTVisitor()

    def interpret(self):
        self.parser.operations()
        self.ast_visitor.visit(self.parser.ast)
