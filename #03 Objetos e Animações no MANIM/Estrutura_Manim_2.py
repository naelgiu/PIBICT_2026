from manim import *

class Estrutura_Manim_2(Scene):
    def construct(self):

        # Define a cor azul para os títulos
        Azul = "#5F86D9"

        # Cria o parágrafo com os títulos e descrições
        texto = Paragraph(
            "Cena: É a tela principal onde você cria e organiza",
            "seus objetos e animações.\n",
             
            "Objetos: São os elementos que você adiciona ao seu vídeo,",
            "como textos, imagens, formas geométricas, etc.\n",
            
            "Animações: São os movimentos e transições que dão vida",
            "aos seus objetos.",
            
            line_spacing=1.2,
            alignment="left",
            
            # Define o estilo de destaque em negrito para os títulos
            t2w={
                "Cena:": BOLD, 
                "Objetos:": BOLD, 
                "Animações:": BOLD
            },
            
            # Aplica a cor de destaque apenas nos títulos
            t2c={
                "Cena:": Azul,
                "Objetos:": Azul,
                "Animações:": Azul
            }
        )

        
        # Reduz o tamanho geral para garantir margens seguras na tela
        texto.scale(0.65)
        

        # Executa a animação de esmaecimento do texto
        self.play(FadeIn(texto[0], texto[1]), run_time=2)
        self.wait(3)

        self.play(FadeIn(texto[3], texto[4]), run_time=2)
        self.wait(3)

        self.play(FadeIn(texto[6], texto[7]), run_time=2)
        self.wait(3)

        self.play(FadeOut(texto), run_time=2.5)
