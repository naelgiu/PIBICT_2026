# Mudando a aparência de um objeto por meio de MÉTODOS

from manim import *

class ex_02(Scene):
    def construct(self):

        circulo = Circle()

        circulo.scale(3)
#       circulo.set_color(YELLOW)
#       circulo.set_opacity(0.3)
        circulo.set_stroke(color=RED, opacity=1, width=8)
        circulo.set_fill(color=BLUE, opacity=0.5)


        self.play(FadeIn(circulo))
        self.wait()
