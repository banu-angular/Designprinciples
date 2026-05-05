class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
# Example usage:
if __name__ == "__main__":  
    shapes = [Rectangle(5, 10), Circle(7)]
    for shape in shapes:
        print(f"The area of the shape is: {shape.area()}")
# In this design:
# - The `Shape` class is an abstract base class with an `area` method that must be implemented by subclasses.
# - The `Rectangle` and `Circle` classes inherit from `Shape` and provide their own implementations of the `area` method.
# This design adheres to the Liskov Substitution Principle because we can substitute any instance   of `Shape` with an instance of `Rectangle` or `Circle` without affecting the correctness of the program.    
