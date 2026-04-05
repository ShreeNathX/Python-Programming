"""
Inheritance)

Create:
    Vehicle → method start()
    Car inherits from Vehicle
"""

class Vehicle:
    def startV(self):
        print('Starting....')
    
class Car(Vehicle):
    def startC(self):
        pass

c = Car()
c.startV()