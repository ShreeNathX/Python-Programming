"""
What happens here?

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    pass

b = B()
"""

# Throw error as there is no show method in class B
