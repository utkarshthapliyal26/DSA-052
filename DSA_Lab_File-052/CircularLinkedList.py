# circular_linked_list_insertion.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")


# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    print("Original list:")
    cll.display()

    print("Inserting 5 at beginning:")
    cll.insert_at_beginning(5)
    cll.display()

    print("Inserting 40 at end:")
    cll.insert_at_end(40)
    cll.display()
