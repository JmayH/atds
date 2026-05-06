from atds import Vertex, Graph, Queue


def traverse(g,start,finish):
    if finish == None:
        print("Finishing vertex doesn't ist!")
    else:
        current = finish
        while current.get_previous() != None: 
            print
            
def bfs(g,start):

def main():
    g = build_graph()