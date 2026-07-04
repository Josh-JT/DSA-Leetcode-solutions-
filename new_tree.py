import sys 

class Node:
    def __init__(self, x):
        self .data = x
        self.children = []

def addChild(parent,child):
    parent.children.append(child)

def printParent(node, parent):
    if node is None:
        print( str(node.data) + " -> NULL")
    else print(str(node.data) + str(parent.data))
