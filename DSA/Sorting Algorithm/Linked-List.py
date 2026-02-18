class  node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__ (self):
        self.head = None

    def insertlist(self, data):
        if self.head is None:
            self.head = node()
            self.head.data = data
            self.head.next = None
        return

        temp = self.head
        while temp.next:
            temp = temp.next
        
        newNode = node()
        newNode.next = None
        newNode.data = data

        temp.next = newNode
        return head
    
    def display(self):
        temp = self.head
        while self.temp:
            print(self.temp.data)
            self.temp = self.temp.next
    
    def delete(self):
        if self.head:
            self.head = head.next
            return
            

