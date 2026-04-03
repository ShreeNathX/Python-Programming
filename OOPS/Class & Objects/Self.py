class student:
    def set_name(self, name):
        self.name = name        # Store in object
    
    def show_name(self):
        print(self.name)


# Create Objects
s1 = student()
s2 = student()

# Set names
s1.set_name("Rahul")
s2.set_name("Sita")

# Display
s1.show_name()          # Rahul
s2.show_name()          # Sita

"""
What is happening?
    when you do:
    s1.set_name("Rahul")

    Python Converts it to:
    student.set_name(s1, "Rahul")

So:
    self --> s1
    "Rahul" --> goes to name

"""