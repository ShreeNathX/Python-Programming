class A:
    def showA(self):
        print("A")
    
class B:
    def showB(self):
        print("B")

class C(A, B):
    pass

c = C()                 # Method calling
c.showA()               # A
c.showB()               # B