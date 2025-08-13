from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        """Add an element to the rear of the queue."""
        self._data.append(x)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        """Return the front element without removing it."""
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return not self._data

    def size(self):
        """Return the number of elements in the queue."""
        return len(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front element:", q.peek())       # 10
    print("Queue size:", q.size())          # 3
    print("Dequeued:", q.dequeue())         # 10
    print("Dequeued:", q.dequeue())         # 20
    print("Is empty?", q.is_empty())        # False
    print("Dequeued:", q.dequeue())         # 30
    print("Is empty?", q.is_empty())        # True
