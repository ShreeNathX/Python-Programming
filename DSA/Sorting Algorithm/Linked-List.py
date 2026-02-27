class node:
    def __init__(self):
        self.data = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    # if head none then create new node and assign head to it
    # else traverse to the end of the list and add new node there
    def insertLISt(self,data):

        if self.head is None:
            self.head = node()
            self.head.data = data
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = node()
        temp.next.data = data
        
    def displayList(self):
        temp = self.head

        while temp:
            print(temp.data)
            print(temp.next)
            temp = temp.next
    
    def  deleteFromBegining(self):
        if self.head is None:
            print("List is empty")
            return
        
        self.head = self.head.next


obj1 = linkedList()
obj1.insertLISt(10)
obj1.insertLISt(20)
obj1.insertLISt(30)
obj1.insertLISt(40)
obj1.displayList()