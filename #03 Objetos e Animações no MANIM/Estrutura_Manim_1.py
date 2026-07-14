from manim import *

class Estrutura_Manim_1(Scene):
    def construct(self):

        # Define o parágrafo
        texto = Paragraph(
            "Cenas", "Objetos", "Animações",
            font_size=65,
            line_spacing=1.2,
            alignment="center"
        )

        # Define a cor do gradiente para o texto
        texto.set_color_by_gradient(BLUE, GREEN, YELLOW)

        # Executa a animação de escrita do texto
        self.play(Write(texto), run_time=3)
        self.wait(4) 

        self.play(Unwrite(texto), run_time=2)
        self.wait(2)
