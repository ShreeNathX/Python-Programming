class student:
    def __init__(self, name):
        self.name = name
    
s1 = student("Ram")
print(s1.name)


"""
Python does internally:
student.__init__(s1, "Ram")
"""