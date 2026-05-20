#!/usr/bin/env python3
"""
binary_heap_tester.py
This program tests your BinaryHeap class.

@author Richard White
@version 2018-04-25
"""

from atds import *       # import the BinaryTree class

def main():
    print("Testing minHeap binary tree")
    tests_passed = 0
    
    # Test 1 - Creating a binary heap
    print("Instantiating empty BinaryTree object...")
    try:
        bh = BinaryHeap()
        tests_passed += 1
        print("Test 1 passed!")
    except:
        print("Issue creating BinaryTree")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 2 - printing the heap
    print("Printing the heap...")
    try:
        print(bh)
        tests_passed += 1
        print("Test 2 passed")
    except:
        print("Issue calling __repr__")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 3 - inserting a key
    print("Inserting a key...")
    try:
        bh.insert(5)
        tests_passed += 1
        print("Test 3 passed!")
    except:
        print("Issue creating a node")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 4 - inserting more key
    print("Inserting keys 7, 9, and 3...")
    try:
        bh.insert(7)
        bh.insert(9)
        bh.insert(3)
        print("New heap:",bh)
        if bh.__repr__() == "BinaryHeap[0, 3, 5, 9, 7]":
            tests_passed += 1
            print("Test 4 passed!")
        else:
            print("Keys inserted incorrectly")
            print("Expected: BinaryHeap[0, 3, 5, 9, 7]")
    except:
        print("Issue with inserting keys correctly")
    print(str(tests_passed) + "/" + str(10))
 
    # Test 5 - Viewing min value
    print("Checking findMin() method...")
    try:
        min_val = bh.find_min()
        if min_val == 3:
            tests_passed += 1
            print("Test 5 passed!")
        else:
            print("Incorrect min_value found")
    except:
        print("Issue calling the find_min() method")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 6 - Removing a value
    print("Calling the del_min() method")
    try:
        val = bh.del_min()
        if val == 3:
            tests_passed += 1
            print("Test 6 passed!")
        else:
            print("Minimum value not returned")
    except:
        print("Issue deleting the minimum value")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 7 - Checking heap structure
    print("Checking heap structure after deletion...")
    try:
        result = bh.__repr__()
        if result == "BinaryHeap[0, 5, 7, 9]":
            tests_passed += 1
            print("Test 7 passed!")
        else:
            print("Expected BinaryHeap[0, 5, 7, 9]")
            print("Deleting the minimum messed up the heap")
    except:
        print("Issue with print out heap structure")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 8 - checking stack
    print("Checking if heap is empty with .is_empty() and .size()...")
    try:
        if not bh.is_empty() and bh.size() == 3:
            tests_passed += 1
            print("Test 8 passed!")
        else:
            print("Problem with .is_empty() or .size()")
    except:
        print("Issue with .is_empty() or .size()")
    print(str(tests_passed) + "/" + str(10))
    
    # Test 9 - inserting a key
    print("Emptying stack and checking .is_empty()...")
        
    bh.del_min()
    bh.del_min()
    bh.del_min()
    if bh.is_empty() and bh.size() == 0:
        tests_passed += 1
        print("Test 9 passed!")
    else:
        print("Issue with .is_empty() or .size()")
    '''
    except:
        print("Issue with .is_empty() or .size()")
    '''
    print(str(tests_passed) + "/" + str(10))
    

    # Test 10 - inserting a key
    print("Testing buildHeap method...")
    values = [2, 3, 9, 4, 1, 8, 7, 15, 20, 41, 32, 5]
    print("Array:",values)
    print("Building heap...")
    bh.build_heap(values)
    print("Resulting heap:",bh)
    if bh.__repr__() == "BinaryHeap[0, 1, 2, 5, 4, 3, 8, 7, 15, 20, 41, 32, 9]":
        tests_passed += 1
        print("Test 10 passed!")
    print(str(tests_passed) + "/" + str(10))
    
if __name__ == "__main__":
    main()