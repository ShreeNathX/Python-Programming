class student:
    def __init__(self, name = "Unknown", age = 18):
        self.name = name
        self.age = age
    
s1 = student()
s2 = student("Ram", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)

"""
Output:
Unknown 18
Ram 20
"""