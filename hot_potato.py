__author__ = "Jamie Hsieh"
__version__ = "02/17/26"
from atds import Queue
def main():
    q = Queue()
    for person in ["Elissa", "Iris", "Evan", "Jamie", "August", "Ethan"]:
        q.enqueue(person)
    print("Original queue/circle")
    print(str(q))
    while q.size() > 1:
        for i in range(6):
            person = q.dequeue()
            print(person, "has the potato!")
            q.enqueue(person)
        person = q.dequeue()
        print(person, "has the potato and is OUT!")
    person = q.peek()
    print(person, "is the winner!")
if __name__ == "__main__":
    main()