from manim import *
import numpy as np


class AxesExample(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-4, 4],
            y_range=[-2, 2],
            axis_config={"include_numbers": True}
        )

        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        label = MathTex(r"y=\sin(x)").next_to(graph, UP)

        self.play(
            Create(axes),
        )
        self.wait(1)
        self.play(
            Create(graph),
            Write(label)
        )


        self.wait(2)