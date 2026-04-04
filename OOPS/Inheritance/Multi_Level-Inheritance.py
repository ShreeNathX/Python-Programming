class A:
    def showA(self):
        print("A")
    
class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")

c = C()
c.showA()           # A
c.showB()           # B
c.showC()           # C

"""
Note: Chain Structure
"""