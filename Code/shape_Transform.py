from manim import *


class TransformShapes(Scene):
    def construct(self):
        title = Text("Transform Animation").to_edge(UP)

        circle = Circle(color=BLUE,fill_opacity=0.5)
        square = Square(color=GREEN,fill_opacity=0.5)

        self.play(Write(title))
        self.play(Create(circle))
        self.wait(1)

        self.play(Transform(circle, square))
        self.wait(1)

        self.play(FadeOut(circle), FadeOut(title))