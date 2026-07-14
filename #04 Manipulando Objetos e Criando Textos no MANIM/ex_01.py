# Mudando a aparência de um objeto por meio de PARÂMETROS

from manim import *

class ex_01(Scene):
    def construct(self):

        quadrado = Square(
            side_length=3,
            fill_opacity=0.5,
#           fill_color=BLUE,
            stroke_opacity=0.5,
#           stroke_color=RED,
            stroke_width=10,
            sheen_factor=0.5,
            color=PURPLE
        )


        self.play(Create(quadrado))
        self.wait()
