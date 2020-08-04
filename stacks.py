class stack:
    def  __init__(self):
        self.stack= []
    #add an element to stack
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    #get the top element of stack
    def peek(self):
        return self.stack[-1]
    #pop from stack
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

stack1= stack()
stack1.add("One")
stack1.add("Two")
stack1.add("Three")
stack1.peek()
print(stack1.peek())
stack1.add("Four")
stack1.add("Five")
print(stack1.peek())
print(stack1.remove())
print(stack1.remove())
