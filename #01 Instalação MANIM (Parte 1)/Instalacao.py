from manim import *

class Installation(Scene):
    def construct(self):
        title = Text("Lista de programas que iremos instalar:").shift(UP*1.2)
        self.play(Write(title))
        self.wait(1)

        steps = [
            "1. Python",
            "2. LaTeX",
            "3. Manim",
            "4. Editor de Código (VS Code)"
        ]

        group = VGroup(*[Text(step, font_size=36) for step in steps]).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=1) 
        self.play(FadeIn(group))
        self.wait(6)
