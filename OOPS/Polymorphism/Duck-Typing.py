"""
If it looks like duck and behaves like a duck, it is a duck.
Means --> When something looks like and behaves like then it is something.

Here, Type doesn't matter, behavior matter.
"""

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

"""
Output:
Bark
Meow
"""
