from manim import *

class Finalizacao(Scene):
    def construct(self):
        text = Text("Obrigado por assistirem!").scale(1.5)
        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text, reverse=False))
        self.wait(1)
