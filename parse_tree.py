#!/usr/bin/env python3

from atds import BinaryTree, Stack
import operator


def build_parse_tree(fpexpr):
    
    tokens = fpexpr.split()
    pt = BinaryTree("")
    parent_stack = Stack()
    parent_stack.push(pt)
    current_focus = pt

    for token in tokens:
        if token == "(":
            current_focus.insert_left("")
            parent_stack.push(current_focus)
            current_focus = current_focus.get_left_child()
        elif token == ")":
            current_focus = parent_stack.pop()
        elif token in "+-*/":
            current_focus.set_root_val(token)
            current_focus.insert_right("")
            parent_stack.push(current_focus)
            current_focus = current_focus.get_right_child()
        else:
            current_focus.set_root_val(float(token))
            current_focus = parent_stack.pop()

    return pt


def evaluate(parse_tree):
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()
    if left_child == None and right_child == None:
        return parse_tree.get_root_val()
    else:
        operator = parse_tree.get_root_val()
        if operator == "+":
            return evaluate(left_child) + evaluate(right_child)
        elif operator == "-":
            return evaluate(left_child) - evaluate(right_child)
        elif operator == "*":
            return evaluate(left_child) * evaluate(right_child)
        elif operator == "/":
            return evaluate(left_child) / evaluate(right_child)

def main():
    EPSILON = 0.001
    tests = [
        ("( 2 + 3 )", 5),
        ("( 1 / 3 )", 1/3),
        ("( ( 3 + 5 ) * 2 )", 16),
        ("( 3 + ( 5 * 2 ) )", 13),
        ("( ( 2 + ( 6 * 7 ) ) - 1 )", 43),
        ("( ( ( ( 4 / 1 ) - ( 4 / 3 ) ) + ( 4 / 5 ) ) - ( 4 / 7 ) )", 3.1416)
    ]

    for i in range(len(tests)):
        print("Testing expression", tests[i][0])
        pt = build_parse_tree(tests[i][0])
        result = evaluate(pt)
        print("Result:", result)

        if abs(result - tests[i][1]) < EPSILON:
            print("Test", i + 1, "passed")
        else:
            print("Test", i + 1, "failed")

    print("""Test 6 should fail. It's an attempt to calculate pi that doesn't 
get very far.""")


if __name__ == "__main__":
    main()