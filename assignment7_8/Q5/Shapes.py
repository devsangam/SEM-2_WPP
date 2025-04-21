PI = 3.14159
from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shapes):
    def __init__(self, length = 0.0):
        self.length = length
    
    def area(self):
        return self.length**2
    
    def perimeter(self):
        return 4 * self.length

class Circle(Shapes):
    def __init__(self, radius = 0.0):
        self.radius = radius
    
    def area(self):
        return PI * (self.radius**2)
    
    def perimeter(self):
        return 2 * PI * self.radius