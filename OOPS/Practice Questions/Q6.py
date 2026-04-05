"""
(Method Overriding)
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Dog")

--> What will Dog().speak() print and why?
"""

# Output will be Dog as it override the Animal's speak method