# Doubly Linked List

#creating a linked list
class Node:
    def __init__(self, data):
        
        self.data= data
        self.next= None
        self.prev= None
class Doubly_linked_list:
    def __init__(self):
        self.head= None
    
    #Adding elements to linked list
    def add1(self, newVal):
        NewNode= Node(newVal)
        NewNode.next= self.head
        if self.head is not None:
            self.head.prev= NewNode
        self.head= NewNode

    # inserting in doubly linked list
    def insert(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

    def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next
#appending elements to the end of the list
    def append(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None):
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return
dlist= Doubly_linked_list()
dlist.add1(1)
dlist.add1(2)
dlist.add1(3)
dlist.insert(dlist.head.next, 13)
dlist.listprint(dlist.head)
dlist.append(45)
dlist.listprint(dlist.head)