from Queue import Queue

user_queue = Queue()
choice = -1
while choice != 0:
    print("1.Enqueue\n2.Dequeue\n3.Peek Queue\n0.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_queue.enqueue()
    elif choice == 2:
        user_queue.dequeue()
    elif choice == 3:
        user_queue.peek()
    elif choice == 0:
        print("Exiting the program...")
    else:
        print("Please enter a valid number\n")
exit(0)
