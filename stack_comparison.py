"""

In our comparison of Stack and UnorderedListStack, I graphed how long it took each stack to do increasingly more push and pop operations. The graph shows that Stack is consistently faster than UnorderedListStack for both push and pop operations. This is most likely because Stack uses Python's built in list, while UnorderedListStack relies on creating individual Node objects which introduces additional overhead. 

"""

#!/usr/bin/env python3
from atds import *
import time
import matplotlib.pyplot as plt


def testStackPush(s: Stack, n: int) -> float:
    stack = s()
    start = time.time()
    for i in range(n):
        stack.push(i)
    stop = time.time()
    return stop-start

def testStackPop(s: Stack, n: int):
    stack = s()
    for i in range(n):
        stack.push(i)
    start = time.time()
    for i in range(n):
        stack.pop()
    stop = time.time()
    return stop-start

def testULSPush(s: UnorderedListStack, n: int):
    stack = s()
    start = time.time()
    for i in range(n):
        stack.push(i)
    stop = time.time()
    return stop-start

def testULSPop(s: UnorderedListStack, n: int):
    stack = s()
    for i in range(n):
        stack.push(i)
    start = time.time()
    for i in range(n):
        stack.pop()
    stop = time.time()
    return stop-start

def main():
    START = 100000
    END = 1000001
    STEP = (END-START) // 10
    x = []
    
    stack_push_times = []
    stack_pop_times = []
    uls_push_times = []
    uls_pop_times = []

    for test_size in range(START, END, STEP):
        x.append(test_size)
        stack_push_times.append(testStackPush(Stack, test_size))
        stack_pop_times.append(testStackPop(Stack, test_size))
        uls_push_times.append(testULSPush(UnorderedListStack, test_size))
        uls_pop_times.append(testULSPop(UnorderedListStack, test_size))

    plt.plot(x, stack_push_times, 'ro', label="Stack push")
    plt.plot(x, stack_pop_times, 'bo', label="Stack pop")
    plt.plot(x, uls_push_times, 'go', label="ULS push")
    plt.plot(x, uls_pop_times, 'yo', label="ULS pop")

    plt.xlabel("Number of operations")
    plt.ylabel("Time in seconds")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()