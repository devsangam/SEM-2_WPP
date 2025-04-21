import math

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def magnitude(self):
        return math.sqrt(self.i**2 + self.j**2)
    
    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.j, self.i))
    
    def distance(self, other):
        return math.sqrt((self.i - other.i)**2 + (self.j - other.j)**2)
    
    def dot_product(self, other):
        return self.i * other.i + self.j * other.j
    
    def cross_product(self, other):
        return self.i * other.j - self.j * other.i
    
    def __repr__(self):
        return f"Vector2D({self.i}, {self.j})"

class Vector3D(Vector2D):
    def __init__(self, x, y, k):
        super().__init__(x, y)
        self.k = k
    
    def magnitude(self):
        return math.sqrt(self.i**2 + self.j**2 + self.k**2)
    
    def distance(self, other):
        return math.sqrt((self.i - other.i)**2 + (self.j - other.j)**2 + (self.k - other.k)**2)
    
    def dot_product(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k
    
    def cross_product(self, other):
        return Vector3D(
            self.j * other.k - self.k * other.j,
            self.k * other.i - self.i * other.k,
            self.i * other.j - self.j * other.i
        )
    
    def __repr__(self):
        return f"Vector3D({self.i}, {self.j}, {self.k})"
