class A:
    def showA(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()

b.showA()               # A
c.showA()               # A

"""
Note: One parent --> Multiple child
"""

