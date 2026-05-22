from manim import *

class ShapeCircle(Scene):
    def construct(self):
        circle = Circle(radius=2,color=RED)
        self.play(Create(circle))
        self.wait(2)

class ShapeSquare(Scene):
    def construct(self):
        circle = Circle(radius=2,color=RED)
        self.play(Create(square))
        self.wait(2)

class ShapeTriangle(Scene):
    def construct(self):
        triangle = Triangle(color=PURPLE)
        self.play(Create(triangle))
        self.wait(2)

class Shapes(Scene):
    def construct(self):
        circle = Circle(radius=1,color=RED)
        square = Square(color=PINK)
        triangle = Triangle(color=PURPLE)

        square.shift(LEFT*3)
        triangle.shift(RIGHT*3)

        self.play(Create(circle))
        self.wait(1)
        self.play(Create(square))
        self.wait(1)
        self.play(Create(triangle))
        self.wait(2)

        self.play(FadeOut(circle),FadeOut(square), FadeOut(triangle))