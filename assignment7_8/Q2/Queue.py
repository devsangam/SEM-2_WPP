class Queue:
    queue = []
    def __init__(self, *args):
        for arg in args:
            self.queue.append(int(arg))
        print("Queue successfully created\n")

    def enqueue(self):
        self.queue.append(int(input("Enter you data: ")))
        print("\nData Enqueued!\n")

    def dequeue(self):
        if len(self.queue) != 0:    
            self.queue.pop(0)
            print("\nData Dequeued!\n")
        else:
            print("\nUnderflow\n")

    def peek(self):
        if len(self.queue) != 0:
            print(self.queue[0])
        else:
            print("\nYou cannot display a empty queue!\n")