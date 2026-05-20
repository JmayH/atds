#!/usr/bin/env python3

from atds import BinaryTree


def preorder(tree):
    values = []
    if tree != None:
        values.append(tree.getRootVal())
        values += preorder(tree.getLeftChild())
        values += preorder(tree.getRightChild())
    return values


def inorder(tree):
    values = []
    if tree != None:
        values += inorder(tree.getLeftChild())
        values.append(tree.getRootVal())
        values += inorder(tree.getRightChild())
    return values


def postorder(tree):
    values = []
    if tree != None:
        values += postorder(tree.getLeftChild())
        values += postorder(tree.getRightChild())
        values.append(tree.getRootVal())
    return values


def main():
    bt = BinaryTree('a')

    bt.insertLeft('b')
    bt.insertRight('c')
    bt.getLeftChild().insertLeft('d')
    bt.getLeftChild().insertRight('e')
    bt.getRightChild().insertLeft('f')
    bt.getRightChild().insertRight('g')
    bt.getLeftChild().getLeftChild().insertLeft('h')
    bt.getLeftChild().getLeftChild().insertRight('i')
    bt.getLeftChild().getRightChild().insertRight('j')
    bt.getRightChild().getRightChild().insertLeft('k')
    print("Preorder:")
    print(preorder(bt))

    print("\nInorder:")
    print(inorder(bt))

    print("\nPostorder:")
    print(postorder(bt))


if __name__ == "__main__":
    main()