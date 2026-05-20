from atds import Vertex, Graph, Queue

def one_letter_off(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

def build_graph(word_file):
    with open(word_file, 'r',encoding='utf-8') as infile:
        words = [line.strip() for line in infile.readlines()]
    # initialize empty graph
    g = Graph()

    # Go through the word list to find all connected words
    for word1 in words:
        for word2 in words:
            if one_letter_off(word1, word2):
                # create vertices while adding edgea
                g.add_edge(word1, word2)
    '''
    # Checking
    for v in g:
        print(v)
        input()
    '''
    return g

def traverse(g, start, finish):
    """Works backwards from the finish vertex, following `previous` vectors
    all the way to the start.
    """
    if finish == None:
        print("Finishing vertex doesn't exist!")
    else:
        current = finish
        while current.get_previous() != None:
            print(current.get_key(), current.get_distance())
            current = current.get_previous()
        if current == start:
            print(current.get_key()) # The last ie. first item in the path
        else:
            print("Couldn't find a path!")

def bfs(g, start):
    start.set_distance(0)
    start.set_previous(None)
    current = start
    q = Queue()
    q.enqueue(current)
    while not q.is_empty():
        current = q.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.get_color() == 'white':
                neighbor.set_color('gray')
                neighbor.set_distance(current.get_distance() + 1)
                neighbor.set_previous(current)
                q.enqueue(neighbor)
        current.set_color('black') 

def main():
    g = build_graph("three-letter_words.txt")
    bfs(g, g.get_vertex("CAP"))
    for v in g:
        print(v.__repr__(), v.get_distance(), v.get_previous())
    traverse(g, g.get_vertex("CAP"), g.get_vertex("PAN"))

main()


