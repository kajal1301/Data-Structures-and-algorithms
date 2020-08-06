import collections

#create an empty dequeue
d= collections.deque()

#adding elements to right side of deque
d.append(1)
d.append(2.4)
d.append('python')
print(d)

#adding elements to the left of deque
d.appendleft('hello world')
d.appendleft(123)
print(d)
#deleting element from right side
d.pop()
print(d)

#deleting element from left side
d.popleft()
print(d)