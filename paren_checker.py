__author__ = "Jamie Hsieh"
__version__ = "02/17/26"
import atds
def is_valid(expr):
    result = True
    temp = atds.Stack()
    for c in expr:
        if c == "(":
            temp.push(c)
        elif c == ")":
            if temp.is_empty():
                result = False
            else:
                temp.pop()
    if not temp.is_empty():
        result = False
    return result