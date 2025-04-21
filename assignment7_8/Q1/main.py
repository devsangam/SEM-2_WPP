from LinkedList import LinkedList
user_linked_list = LinkedList()
choice = -1
while choice != 0:
    print("1.Insert Node\n2.Delete Node\n3.Display Linked List\n0.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_linked_list.insert_node()
    elif choice == 2:
        user_linked_list.delete_node()
    elif choice == 3:
        user_linked_list.display_linked_list()
    elif choice == 0:
        print("Exiting the program...")
    else:
        print("Please enter a valid number\n")
exit(0)
