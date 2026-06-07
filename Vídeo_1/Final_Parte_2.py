from manim import *

class Intermediador(Scene):
    def construct(self):
        texto = Text("Espero você para a parte 2 do vídeo!", font_size=60)
        self.play(Write(texto))
        self.play(Indicate(texto, color=WHITE, scale_factor=1.1))
        self.wait(3)
        self.play(Unwrite(texto, reverse=False)) 
        self.wait(1)
