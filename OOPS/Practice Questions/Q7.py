"""
Create class Calculator using *args to add numbers
"""

class Calculator:
    def add(self, *args):
        print(sum(args))
    
c = Calculator()
c.add(20, 40)       # 60
c.add(5, 12, 8)     # 25