class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if self.head is None:
            return
        
        current = self.head
        prev = None

        # case 1: delete head node
        if current.data == key:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # case 2: delete non-head
        current = self.head.next
        prev = self.head
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def print_list(self):
        if not self.head:
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Example
cll = CircularLinkedList()
for x in [10, 20, 30, 40]:
    cll.append(x)
    
print("Before deletion:")
cll.print_list()

cll.delete(30)

print("After deletion:")
cll.print_list()
