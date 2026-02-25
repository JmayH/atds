#!/usr/bin/env python3

"""
paren_tester.py
The paren_tester program imports a student's paren_checker.py program which 
defines a function is_valid(string). That function takes a string of 
parentheses as a parameter and returns True if the parentheses are "well-formed",
and False otherwise.

The paren_checker.py program should use a Stack object to check the parentheses.
"""

import paren_checker

def main():
    testsPassed = 0

    try:
        if paren_checker.is_valid("(((())))") == True:
            testsPassed += 1
            print("Test 1 passed")
        else:
            print("Test 1 failed")
    except:
        print("Test 1 broke the tester")

    try:
        if paren_checker.is_valid("(((()))") == False:
            testsPassed += 1
            print("Test 2 passed")
        else:
            print("Test 2 failed")
    except:
        print("Test 2 broke the tester")
    
    try:
        if paren_checker.is_valid("(()))(") == False:
            testsPassed += 1
            print("Test 3 passed")
        else:
            print("Test 3 failed")
    except:
        print("Test 3 broke the tester")

    try:
        if paren_checker.is_valid("(()(()()))")== True:
            testsPassed += 1
            print("Test 4 passed")
        else:
            print("Test 4 failed")
    except:
        print("Test 4 broke the tester")

    try:
        if paren_checker.is_valid("(()(()()))") == True:
            testsPassed += 1
            print("Test 5 passed")
        else:
            print("Test 5 failed")
    except:
        print("Test 5 broke the tester")

    try:
        if paren_checker.is_valid(")))(((") == False:
            testsPassed += 1
            print("Test 6 passed")
        else:
            print("Test 6 failed")
    except:
        print("Test 6 broke the tester")

    try:
        if paren_checker.is_valid("()") == True:
            testsPassed += 1
            print("Test 7 passed")
        else:
            print("Test 7 failed")
    except:
        print("Test 7 broke the tester")
    try:
        if paren_checker.is_valid("(") == False:
            testsPassed += 1
            print("Test 8 passed")
        else:
            print("Test 8 failed")
    except:
        print("Test 8 broke the tester")

    try:
        if paren_checker.is_valid(")") == False:
            testsPassed += 1
            print("Test 9 passed")
        else:
            print("Test 9 failed")
    except:
        print("Test 9 broke the tester")
        
    try:
        if paren_checker.is_valid("(9)") == True:
            testsPassed += 1
            print("Test 10 passed")
        else:
            print("Test 10 failed")
    except:
        print("Test 10 broke the tester")

    try:
        if paren_checker.is_valid("{[( )]}") == True:
            testsPassed += 1
            print("Fancy Test 11 passed")
        else:
            print("Fancy Test 11 failed")
    except:
        print("Fancy Test 11 broke the tester")
        
    try:
        if paren_checker.is_valid("[( { )[()])") == False:
            testsPassed += 1
            print("Fancy Test 12 passed")
        else:
            print("Fancy Test 12 failed")
    except:
        print("Fancy Test 12 broke the tester")
    
    print(str(testsPassed) + "/12 tests passed")


if __name__ == "__main__":
    main()
