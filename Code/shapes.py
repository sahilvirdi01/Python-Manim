# from manim import *

# class FirstScene(Scene):
#     def construct(self):
#         # This is where all the magic happens
#         circle = Circle(radius=2, color=BLUE)
#         self.play(Create(circle))
#         self.wait(2)          # Wait 2 seconds
        


from manim import *

class ShapeCircle(Scene):
    def construct(self):
        circle = Circle(radius=2,color=RED)
        self.play(Create(circle))
        self.wait(2)