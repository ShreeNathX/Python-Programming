"""
Methods that do not depend on class or instance variable
Use decorator: @staticmethod
"""

class math:
    @staticmethod
    def add(a, b):              # No self and no cls
        return a + b
    
print(math.add(10, 15))         # 25