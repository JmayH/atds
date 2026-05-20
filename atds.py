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
    def search(self, item):
        current = self.head
        while(current.get_data() != item and current.get_next() != None):
            current = current.get_next()
        if current.get_data() == item:
            return True
        else:
            return False
    
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
    def pop(self, pos=None):
        if pos is None:
            pos = self.length() - 1
        if pos == 0:
            if self.head != None:
                item = self.head.get_data()
                self.head = self.head.get_next()
                return item
        else:
            previous = None
            current = self.head
            count = 0
            while current != None and count < pos:
                previous = current
                current = current.get_next()
                count += 1
            if current != None:
                item = current.get_data()
                previous.set_next(current.get_next())
                return item
        return None
    
    def is_empty(self):
        return self.head is None
    
    def append(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
                
    def index(self,item):
        count = 0
        current = self.head
        while current != None:
            if current.get_data() == item:
                return count
            else:
                current = current.get_next()
                count += 1
    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            previous = None
            current = self.head
            count = 0
            while current != None and count < pos:
                previous = current
                current = current.get_next()
                count += 1
            previous.set_next(new_node)
            new_node.set_next(current)
    
    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                if self.search(item) == True:
                    self.remove(item)
                return
            else:
                previous = current
                current = current.get_next()    

        
        return
    
    
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
        
        
 
class HashTable(object):
    def __init__(self, m):
        self.m = m
        self.keys = m * [None]
        self.values = m *[None]
        self.entries = 0
        
    def hash_function(self, key, m):
        return key % m
    def __len__(self):
        return self.entries
    def put(self, key, value):
        hash = self.hash_function(key, self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m 
        if self.keys[hash] == None:
            self.entries += 1
        self.keys[hash] = key
        self.values[hash] = value
       
    def get(self,key):
        hash = self.hash_function(key,self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m
        return self.values[hash]
    def __repr__(self):
        return str(self.keys) + "\n" + str(self.values)
   
class BinaryTree:
    def __init__(self, key):
        self.root_val = key
        self.left_child = None
        self.right_child = None

    def get_root_val(self):
        return self.root_val

    def set_root_val(self, new_val):
        self.root_val = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, new_left_child):
        new_tree = BinaryTree(new_left_child)
        if self.left_child != None:
            new_tree.left_child = self.left_child
        self.left_child = new_tree

    def insert_right(self, new_right_child):
        new_tree = BinaryTree(new_right_child)
        if self.right_child != None:
            new_tree.right_child = self.right_child
        self.right_child = new_tree

    def __str__(self):
        left = str(self.left_child)
        if self.left_child == None:
            left = "None"
        right = str(self.right_child)
        if self.right_child == None:
            right = "None"
        return f"BinaryTree({self.root_val}, {left}, {right})"
    
class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is connected.
        """
        self.key = key
        self.neighbors = {}   # empty dictionary for neighboring vertices. key is
                              # the Vertex, value is the weight
        self.color = 'white'
        self.distance = 0
        self.previous = None

    def set_neighbor(self, other, weight=0):
        """Adds a reference to a neighboring Vertex object `other` to the dictionary, 
        to which this vertex is connected by an edge. If a weight is not indicated, 
        default weight is 0.
        """
        self.neighbors[other] = weight

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_distance(self):
        return self.distance
    
    def set_distance(self, new_distance):
        self.distance = new_distance

    def get_previous(self):
        return self.previous
    
    def set_previous(self, new_prev):
        self.previous = new_prev

    def __repr__(self):
        """Returns a representation of the vertex and its neighbors, suitable for 
        printing. Check out the example of 'list comprehension' here!
        """
        return f"Vertex({self.key})"
        
    def __str__(self):
        return ( f"{self.key} (color={self.color}), connected to: "
        + f"{[x.key for x in self.neighbors]}")

    def get_neighbors(self):
        return self.neighbors.keys()    # returns Vertex objects

    def get_key(self):
        return self.key

    def get_neighbor(self, other):
        """Returns the weight of an edge connecting this vertex with another,
        or None if the neighbor doesn't exist
        """
        return self.neighbors.get(other, None)
    
class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        '''
        # This is the classic way of doing that
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None
        '''
        # Single-line alternative
        return self.vertices.get(key, None)

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        # if the to_key doesn't yet have a vertex, create it
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        # now we can create the edge between the two
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.vertices.values())

class BinaryHeap():

    def __init__(self):
        self.heap_list = [0]
        
    def insert(self, value):
        self.heap_list.append(value)
        self.percolate_up(self.size())

    def percolate_up(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.heap_list[i] < self.heap_list[parent]:
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            i = parent

    def del_min(self):
        if self.is_empty():
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        if not self.is_empty():
            self.percolate_down(1)

        return min_value

    def percolate_down(self, i):
        while i * 2 <= self.size():
            min_child = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = \
                    self.heap_list[min_child], self.heap_list[i]

            i = min_child

    def min_child(self, i):
        left_child = i * 2
        right_child = i * 2 + 1

        if right_child > self.size():
            return left_child
        else:
            if self.heap_list[left_child] < self.heap_list[right_child]:
                return left_child
            else:
                return right_child

    def find_min(self):
        if self.is_empty():
            return None
        return self.heap_list[1]

    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        self.heap_list = [0] + list_of_keys[:]

        i = self.size() // 2

        while i > 0:
            self.percolate_down(i)
            i -= 1

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)


def main():
    print("Demonstrating minHeap binary tree")

    bh = BinaryHeap()

    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(1)
    bh.insert(50)
    bh.insert(15)

    print("Heap after insertions:")
    print(bh)

    print("Minimum value:")
    print(bh.find_min())

    print("Deleted minimum:")
    print(bh.del_min())

    print("Heap after deleting minimum:")
    print(bh)

    print("\nBuilding heap from list:")
    bh2 = BinaryHeap()
    bh2.build_heap([9, 5, 6, 2, 3])

    print(bh2)
    print("Minimum value:")
    print(bh2.find_min())

if __name__ == "__main__":
    main()