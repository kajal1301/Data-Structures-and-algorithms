class Queue:
    def __init__(self):
        self.queue= list()

    #Adding Elements to a Queue
    def addToQueue(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    
    #Removing Elements from a queue:
    def removeFromQueue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("Queue is Empty")

    def size(self):
        return len(self.queue)
q= Queue()
q.addToQueue("One")
q.addToQueue("Two")
q.addToQueue("Three")
print(q.size)
print(q.removeFromQueue())
print(q.removeFromQueue())

