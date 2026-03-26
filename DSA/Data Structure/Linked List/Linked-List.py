class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertlist(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    
    def insertAtPosition(self, pos, data):
        if pos < 0:
            print("Invalid Position...")
            return
        
        newNode = Node(data)
        
        # If inserting at beginning
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        temp = self.head
        count = 0
        
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        
        if not temp:
            print("Position out of range...")
            return
        
        newNode.next = temp.next
        temp.next = newNode
    
    def displayList(self):
        if not self.head:
            print("Empty List..")
            return
        
        temp = self.head
        print('Displaying the elements of list...')
        while temp:
            print(f'{temp.data}')
            temp = temp.next


# Example usage
l1 = LinkedList()
l1.insertlist(10)
l1.insertlist(20)
l1.insertlist(30)
l1.insertAtBeginning(5)
l1.insertAtPosition(2, 15)
l1.insertAtEnd(40)
l1.displayList()