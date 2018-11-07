import os
from interpreter import *

if __name__ == '__main__':
    path = input()
    path = os.path.realpath(path)
    with open(path) as p:
        read_data = p.read()
    interpreter = Interpreter(read_data)
    interpreter.interpret()
