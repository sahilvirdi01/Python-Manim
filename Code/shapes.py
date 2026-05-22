from manim import *

class ShapeCircle(Scene):
    def construct(self):
        circle = Circle(radius=2,color=RED)
        self.play(Create(circle))
        self.wait(2)