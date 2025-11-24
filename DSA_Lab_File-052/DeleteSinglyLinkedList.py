class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next
        print("Node deleted from beginning.")

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
            print("Deleted the only node in the list.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        print("Node deleted from end.")

    def delete_value(self, key):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.data == key:
            self.head = self.head.next
            print(f"Node with value {key} deleted from list.")
            return
        prev = None
        temp = self.head
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"Value {key} not found in list.")
            return
        prev.next = temp.next
        print(f"Node with value {key} deleted from list.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    for x in [10, 20, 30, 40]:
        ll.insert_at_end(x)
    ll.display()

    ll.delete_beginning()
    ll.display()

    ll.delete_end()
    ll.display()

    ll.delete_value(20)
    ll.display()
