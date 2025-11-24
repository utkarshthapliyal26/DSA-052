class CircularQueue:
    def __init__(self, maxsize=5):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.maxsize == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.maxsize
        self.queue[self.rear] = value
        print(f"Enqueued element: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.maxsize
        print(f"Dequeued element: {element}")
        return element

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Elements in queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.maxsize
        print()

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.display()
