__author__ = 'sean'

class Node:
    left, right, loc = None, None, None
    def __init__(self, loc):
        self.left = None
        self.right = None
        self.loc = loc

class OrdTree:
    root = None
    def __init__(self):
        self.root = None
    def addNode(self, loc):
        return Node(loc)
    def insert(self, root, loc):
        #inserts new data
        if root == None:
            #isn't any data, adds it and returns
            n = Node(loc)
            self.root = n
            return n
        else:
            #enters into the tree
            locy = loc[0]
            rooty = root.loc[0]
            if(locy <= rooty):
                #goes into the left
                root.left = self.insert(root.left, loc)
            else:
                #process the right tree
                root.right = self.insert(root.right, loc)
            return root
