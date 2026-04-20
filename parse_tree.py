__author__ = "Jamie Hsieh"
__version__ = "4/15/26"

from atds import BinaryTree, Stack 

def build_parse_tree(tokens: list) -> BinaryTree:
    bt = BinaryTree(None)
    st = Stack()
    current = bt
    st.push(current)
    
    for token in tokens:
        if token == "(":
            current.insert_left(None)
            st.push(current)
            current = current.get_left_child()
            print(current)
        elif token in ('+-*/'):
            current.set_root_val(token)
            current.insert_right(None)
            st.push(current)
            current = current.get_right_child()
        elif token == ")":
            current = st.pop()
        else:
            current.set_root_val(int(token))
            current = st.pop()
    return bt
def main():
    fpe = "( 2 * 3 )"
    tokens = fpe.split("")
    build_parse_tree(tokens)
    print(bt)
    
if __name__ == "__main__":
    main()
