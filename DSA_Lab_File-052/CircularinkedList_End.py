class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")

    def delete_begin(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = self.head.next
        self.head = self.head.next
        print("Node deleted from beginning.")

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head
        print("Node deleted from end.")


# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    for x in [10, 20, 30, 40]:
        cll.insert(x)

    print("Initial List:")
    cll.display()

    print("Delete from beginning:")
    cll.delete_begin()
    cll.display()

    print("Delete from end:")
    cll.delete_end()
    cll.display()
