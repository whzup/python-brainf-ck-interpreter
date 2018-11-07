# A simple Brainf*ck interpreter

This is a simple Brainf*ck interpreter written in Python.
It uses a LL(1) recursive descent lexer to tokenize the input and a
LL(1) recursive descent parser to create an AST which is the traversed
by a simple visitor which interprets the code.