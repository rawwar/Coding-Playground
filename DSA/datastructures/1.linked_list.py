class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def insert_tail(self, data):
        curr = self.head
        if curr is None:
            self.head = Node(data)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
    
    def is_empty(self):
        if not self.head:
            return True
        return False

    def search(self, data):
        
        curr = self.head

        while curr:
            if curr.data == data:
                return curr
            else:
                curr = curr.next
    
    def delete_node(self, data):
        curr = self.head

        if curr.data == data:
            self.head = None
            return True
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True
         
        