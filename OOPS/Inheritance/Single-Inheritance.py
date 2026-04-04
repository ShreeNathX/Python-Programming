class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

b = B()
b.showA()               # A
b.showB()               # B

"""
Note: One parent --> One child
"""