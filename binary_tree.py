#Binary Tree in python

#Creating root node
class Node:
    def __init__(self,data):
        self.left= None
        self.right= None
        self.data= data
    #Inserting in a tree
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #Searching for a value in Btree
    def search(self,s):
        if s < self.data:
            if self.left is None:
                return str(s)+" Not Found"
            return self.left.search(s)
        elif s > self.data:
            if self.right is None:
                return str(s)+" Not Found"
            return self.right.search(s)
        else:
            print(str(self.data) + ' is found')
    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.data),
        if self.right:
            self.right.printTree()
root= Node(100)
root.printTree()
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print(root.search(7))
print(root.search(14))