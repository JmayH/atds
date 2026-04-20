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
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"
    
class UnorderedList():
    def __init__(self):
        self.head = None
    def add(self,item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    def peek(self):
        if self.head is None:
            return None
        return self.head.get_data()
    
    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
    def length(self):
        node_count = 0                  
        current = self.head            
        while current != None:          
            current = current.get_next()   
            node_count += 1                
        return node_count
    def pop(self):
        if self.head is None:
            return None
        current = self.head
        self.head = current.get_next()
        return current.get_data()
    
    def is_empty(self):
        return self.head is None
    
    def remove(self,data):
        previous = None                         
        current = self.head                     
        while current != None:              
            if current.get_data() == data:     
                if previous == None:            
                    self.head = current.get_next()      
                else:
                    previous.set_next(current.get_next()) 
                                              
                return                         
            else:
                previous = current             
                current = current.get_next()  
     
class UnorderedListStack(object):
    def __init__(self):
        self.uls = UnorderedList()
    def push(self,item): 
        self.uls.add(item)
    def pop(self):
        return self.uls.pop()
    def peek(self):
        item = self.uls.peek()
    def size(self):
        return self.uls.length()
    def is_empty(self):
        return self.uls.is_empty()
    
class LinearSearcher():
    def search(self, list, num):
        for i in range(len(list)):
            if list[i] == num:
                return i
        return None
class BinarySearcher():
    def search(self, list, num):
        low = 0
        high = len(list)-1
        while low <= high:
            middle = (low + high)//2
            if list[middle] == num:
                return middle
            elif num <= list[middle]:
                high = middle-1
            else:
                low = middle + 1
        return None
        
        
'''     
class HashTable(object):
    def __init__(self, m):
        self.m = m
        self.keys = m * [None]
        self.values = m *[None]
        
    def hash_function(self, key, m):
        return key % m
    
    def put(self, key, value):
        hash = self.hash_function(key, self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m 
        self.keys[hash] = key
        self.values[hash] = value
        if self.keys[hash] == None:
            self.entries += 1
    def get(self,key):
        hash = self.hash_function(key,self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            
    def __repr__(self):
        return self.keys + "\n" + self.values
 '''       
                
def main():
    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")
    
    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(10, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")
    
    print("\nTEST: Trying to print the current state of table...")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, None, 10]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, None, 'f']")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")
    
    print("\nTEST: Using put() for a function at the end of the table to see if it wraps around...")
    try:
        h.put(21, "g")
        if h.get(21) == "g":
            print("SUCCESS. .put() correctly wrapped in the table.")
            tests_passed += 1
        else:
            print("FAIL. .put() wraparound didn't work.")
        print(h)
    except:
        print("FAIL. .put() didn't correctly wrap the table in linear probe.")
    
    print("\nTEST: Checking the number of values in the hash table...")
    try:
        l = len(h)
        if l == 6:
            print("SUCCESS. len(h) is 6.")
            tests_passed += 1
        else:
            print("FAIL. len(h) should have been 5 -- solution is to write a __len__ method.")
    except:
        print("FAIL. Problem with len() method.")
    
    print("\nTEST: Looking for original hash in table...")
    try:
        result = h.get(10)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Replacing original hash {1, 'a'} in table with {1, 'z'}...")
    try:
        h.put(1, "z")
        result = h.get(1)
        if result == "z":
            print("SUCCESS. New value put and found.")
            tests_passed += 1
        else:
            print("FAIL. New value not put/found.")
    except:
        print("FAIL. Problem with replacing an old key.")
    
    print("\nTEST: Looking for key-collision in table...")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() finding a key-collision.")
    
    print("\nTEST: Looking for a hash that's not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Looking for collision not in table...")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nResults:")
    print(tests_passed,"/ 12 tests passed")
if __name__ == "__main__":
    main()