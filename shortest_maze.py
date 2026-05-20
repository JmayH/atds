from atds import Vertex, Graph, Queue
class MazeVertex(Vertex):
    def __init__(self, key,value):
        super().__init__(key)
        self.value = value()
        
    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value
    def __repr__(self):
        return super().__repr__() + "value=" + str()
        
def build_graph(maze_file):
    with open(maze_file, 'r', encoding = 'utf-8') as infile:
        maze = [line.strip() for line in infile.readlines()]
    for row in range(len(maze)):
        maze[row] = [char for char in maze[row]]
 
            
    g = Graph()
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "X" or maze[row][col] == "Y" or maze[row][col] == " ":
                v = MazeVertex((row,col), maze)
                
    return g

def traverse(g, start, finish):
    """Works backwards from the finish vertex, following `previous` vectors
    all the way to the start.
    """
    if finish != None:
        current = finish
        while current.get_previous() != None:
            print(current.get_key(), current.get_distance())
            current = current.get_previous()
        if current == start:
            print(current.get_key()) # The last ie. first item in the path
        else:
            print("Couldn't find a path!")