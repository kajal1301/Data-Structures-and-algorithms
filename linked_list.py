# Linked List in Python

#Creating a Linked List
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class ll:
    def __init__(self):
        self.head= None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


list= ll()
list.headval= Node("Name1")
a= Node("Name2")
b= Node("Name3")
list.headval.nextval= a
a.nextval= b

# Traversing a LinkedList
list.listprint()

#Insertion in a Linked List
list.AtBegining("Name4")
list.listprint()

#Insertion at the end of Linked List
list.AtEnd("Name5")
list.listprint()

#Inserting in between two Data Nodes

list.Inbetween(list.headval.nextval,"Name6")

list.listprint()