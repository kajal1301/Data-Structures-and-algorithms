#Heaps in Python:
# Heap is a tree Data structure where each parent node is less than or equal to its child node. This is called Min Heap.
# If each parent node is greater than or equal to child node then it is called Max Heap.

# Creating a Heap: It is created by inbuild functon in python "heapq".
import heapq
H= [1, 14, 21, 22, 0, 54]

#To arrange elements we use heapify
heapq.heapify(H)
print(H)

#Inserting into heap
heapq.heappush(H,9)
print(H)

#Removing from heap
#It always remove the function at index 1
heapq.heappop(H)
print(H)

#Replace an element
#It removes the smallest element of heap and insert new element at some place
heapq.heapreplace(H,8)
print(H)

