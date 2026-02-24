__author__ = "Jamie Hsieh"
__version__ = "2026-02-12"

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0
    def __repr__(self):
        return str(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)

class Deque():
    def __init__(self):
        self.queue = []
    def add_front(self, item):
        self.queue.insert(0,item)
    def add_rear(self,item):
        self.queue.append(item)
    def remove_front(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    def remove_rear(self):
        if len(self.queue) > 0:
            return self.queue.pop(-1)
    def peek_front(self):
        if len(self.queue) > 0:
            return self.queue[0]
    def peek_rear(self):
        if len(self.queue) > 0:
            return self.queue[-1]
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)
          
        

def main():
    pass
if __name__ == "__main__":
    main()