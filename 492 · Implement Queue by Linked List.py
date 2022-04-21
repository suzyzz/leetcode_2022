# Description
# Implement a Queue by linked list. Support the following basic methods:

# enqueue(item). Put a new item in the queue.
# dequeue(). Move the first item out of the queue, return it. If the queue is empty, returned. -1.、
# Example
# Example 1:

# Input:
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue() // return 1
# enqueue(4)
# dequeue() // return 2
# Example 2:

# Input:
# enqueue(10)
# dequeue()// return 10
# dequeue()// return -1


class Node():
    def __init__(self, _val):
        self.next = None
        self.val = _val

class MyQueue(object):
    def __init__(self):
        self.first, self.last = None, None

    def enqueue(self, item):
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue(self):
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            return item
        return -1
