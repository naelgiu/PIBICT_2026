from manim import *

class teste123(Scene):
    
    def construct(self):
        texto = Text("Hello, world!")

        self.play(Write(texto))
        self.wait(2)
