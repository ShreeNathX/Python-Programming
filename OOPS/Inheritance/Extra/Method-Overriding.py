"""
When child class provides its own implementation of parent method
"""

class Animal:
    def speak(self):
        print("Animal Sound")
    

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()                   # Output: Bark

"""
Here speak method is common in both and when we call speak method then it override the Animal class's speak method.
"""
    