from manim import *

class DrawCircle(Scene):
    def construct(self):
        # Create a circle object
        circle = Circle() 
        
        # Set styling (color and transparency)
        circle.set_fill(RED, opacity=0.5) 
        
        # Animate the drawing of the circle
        self.play(Create(circle)) 
        self.wait(1)
