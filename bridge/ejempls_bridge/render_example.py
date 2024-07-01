from abc import ABC, abstractmethod

# Implementor
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x, y, radius):
        pass

# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# ConcreteImplementor 1
class OpenGLRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"OpenGL: renderizando un círculo en ({x}, {y}) con radio {radius}")

# ConcreteImplementor 2
class DirectXRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"DirectX: renderizando un círculo en ({x}, {y}) con radio {radius}")

# RefinedAbstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, radius: int):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.x, self.y, self.radius)

def main():
    opengl_renderer = OpenGLRenderer()
    directx_renderer = DirectXRenderer()

    circle1 = Circle(opengl_renderer, 10, 20, 5)
    circle2 = Circle(directx_renderer, 15, 25, 10)

    circle1.draw()
    circle2.draw()

if __name__ == "__main__":
    main()
