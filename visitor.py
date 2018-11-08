"""
A simple visitor which can traverse a
homogeneous AST.
"""
from language import *
import logging


class ASTVisitor:
    """Visitor class to visit the nodes of the AST"""
    def __init__(self):
        self.exec_list = [0]
        self.exec_ptr = 0
        self.logger = logging.getLogger(__name__)

    def visit(self, node):
        self.logger.debug("Visited {} node".format(node.token.token_type))
        if node.token.token_type == L_SHIFT:
            self._l_shift()
            self.visit_children(node)
        elif node.token.token_type == R_SHIFT:
            self._r_shift()
            self.visit_children(node)
        elif node.token.token_type == DEC:
            self._dec()
            self.visit_children(node)
        elif node.token.token_type == INC:
            self._inc()
            self.visit_children(node)
        elif node.token.token_type == PUT:
            self._put()
            self.visit_children(node)
        elif node.token.token_type == GET:
            self._get()
            self.visit_children(node)
        elif node.token.token_type == L_PAREN:
            self._loop(node)
        elif node.token.token_type == R_PAREN:
            pass
        else:
            self.visit_children(node)

    def visit_children(self, node):
        if node.children is not None:
            for child in node.children:
                self.visit(child)

    def _l_shift(self):
        self.exec_ptr -= 1
        if self.exec_ptr < 0:
            raise Exception("Execution pointer below memory limit")

    def _r_shift(self):
        self.exec_ptr += 1
        if len(self.exec_list) == self.exec_ptr:
            self.exec_list.append(0)

    def _inc(self):
        self.exec_list[self.exec_ptr] += 1

    def _dec(self):
        self.exec_list[self.exec_ptr] -= 1

    def _put(self):
        print(chr(self.exec_list[self.exec_ptr]), end='', flush=True)

    def _get(self):
        c = int(input("in >"))
        self.exec_list[self.exec_ptr] = chr(c)

    def _loop(self, node):
        while self.exec_list[self.exec_ptr] != 0:
            for child in node.children[0:-1]:
                self.visit(child)
        self.visit(node.children[-1])

