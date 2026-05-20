from atds import Vertex, Graph, Queue
class MazeVertex(Vertex):
    def __init__(self, key,value):
        super().__init__(key)
        self.value = value
        
    def get_value(self):
        return self.value
    def set_value(self, new_value):
        self.value = new_value
    def __repr__(self):
        return "MazeVertex(" + str(self.key) + ", value=" + str(self.value) + ")"
      
def build_graph(maze_file):
    with open(maze_file, 'r', encoding = 'utf-8') as infile:
        maze = [line.strip() for line in infile.readlines()]
    for row in range(len(maze)):
        maze[row] = [char for char in maze[row]]
 
            
    g = Graph()
    start = None
    finish = None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] != "0":
                key = (row, col)
                g.vertices[key] = MazeVertex(key, maze[row][col])

                if maze[row][col] == "X":
                    start = g.get_vertex(key)

                elif maze[row][col] == "Y":
                    finish = g.get_vertex(key)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(len(maze)):
        for col in range(len(maze[row])):

            if (row, col) in g.vertices:

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]

                    if (new_row, new_col) in g.vertices:
                        g.add_edge((row, col), (new_row, new_col))

    return maze, g, start, finish

def bfs(maze,g,start, finish):
    start.set_distance(0)
    start.set_previous(None)
    current = start
    found = False
    q = Queue()
    print("Putting", current, "on the queue")
    q.enqueue(current)
    while not q.is_empty() and not found:
        current = q.dequeue()
        print("just pulled", current.__repr__(), "off the queue!")
        for neighbor in current.get_neighbors():
            print("Checking neighbor", neighbor)
            if neighbor.get_color() == "white":
                neighbor.set_color("gray")
                neighbor.set_distance(current.get_distance() +1)
                neighbor.set_previous(current)
                print("Putting", neighbor, "on the queue")
                q.enqueue(neighbor)
                if neighbor == finish:
                    found = True
        current.set_color("black")
    return found

def traverse(start, finish):
    path = []
    current = finish
    while current != None:
        path.append(current.get_key())
        current = current.get_previous()
    path.reverse()
    if len(path) > 0 and path[0] == start.get_key():
        return path
    else:
        return None

def mark_path(maze, path):
    for coordinate in path:
        row = coordinate[0]
        col = coordinate[1]

        if maze[row][col] != "X" and maze[row][col] != "Y":
            maze[row][col] = "."

def display_maze(maze):
    for row in maze:
        print("".join(row))
        
def main():
    maze_file = "maze.txt"

    maze, g, start, finish = build_graph(maze_file)
    print("Original maze:")
    display_maze(maze)
    found = bfs(maze, g, start, finish)
    if found:
        path = traverse(start, finish)
        print("\nShortest path:")
        print(path)
        print("\nNumber of steps:", len(path) - 1)
        mark_path(maze, path)
        display_maze(maze)
    else:
        print("No path found!")


if __name__ == "__main__":
    main()