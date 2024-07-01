from abc import ABC, abstractmethod

# Implementor
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

# Concrete Implementors
class Red(Color):
    def apply_color(self):
        return "aplicando color rojo"

class Blue(Color):
    def apply_color(self):
        return "aplicando color azul"

# Abstraction
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction 1
class Circle(Shape):
    def draw(self):
        print(f"Círculo: {self.color.apply_color()}")

# Refined Abstraction 2
class Square(Shape):
    def draw(self):
        print(f"Cuadrado: {self.color.apply_color()}")

# Refined Abstraction 3
class Triangle(Shape):
    def draw(self):
        print(f"Triangulo: {self.color.apply_color()}")

# Client Code
def main():
    red = Red()
    blue = Blue()

    circle_red = Circle(red)
    square_blue = Square(blue)
    triangle = Triangle(red)

    circle_red.draw()
    square_blue.draw()
    triangle.draw()

if __name__ == "__main__":
    main()
