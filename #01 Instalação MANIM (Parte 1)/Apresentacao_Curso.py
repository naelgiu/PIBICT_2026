from manim import *

class ApresentacaoCurso(MovingCameraScene):
    def construct(self):
        #CENÁRIO 1
        #Nomes
        nome1 = Text("Bolsista: Natanael Rocha", font_size=30, color=BLUE)
        nome2 = Text("Professor Orientador: Emílio Rodrigues", font_size=30, color=BLUE)
        nomes = VGroup(nome1, nome2).arrange(DOWN, buff=0.2)

        #Projeto
        projeto1 = Text("PIBICT  2026", font_size=50)
        projeto2 = Text("Animações Matemáticas com Python", font_size=50)
        projetos = VGroup(projeto1, projeto2).arrange(DOWN, buff=0.5)


        cena_1 = VGroup(nomes, projetos).shift(LEFT*7)

        self.camera.frame.move_to(cena_1)
        self.wait(1)


        #Animando os nomes
        self.play(Write(nomes, run_time=3))
        self.wait(2)

        #Animando o projeto
        self.play(Succession(
            nomes.animate.shift(DOWN*3),
            AddTextLetterByLetter(projeto1),
            AddTextLetterByLetter(projeto2)
        ))
        self.wait(2)

        #CENÁRIO 2
        
        #Imagens
        Grant_Sanderson = ImageMobject("Grant_Sanderson.png").scale(1.3)
        Logo3b1b = ImageMobject("Logo3b1b.png").scale(0.2)
        logoytb = ImageMobject("logoytb.png").scale(0.2)
        logo_python = ImageMobject("Python.png").scale(0.2)
        logo_manim = ManimBanner()

        #Algumas legendas que faltam
        manim_nome = Text("Biblioteca Manim", font_size=45).next_to(logo_manim.get_center(), DOWN, buff=1)
        b1b_nome = Text("3Blue1Brown", font_size=45).next_to(Logo3b1b.get_center(), DOWN, buff=1)
        nome_grant = Text("Grant Sanderson", color=BLUE,font_size=35)


        #Primeiro grupo de imagens
        imagens_1 = Group(logo_manim, manim_nome).arrange(RIGHT, buff=1).shift(RIGHT*7)

        #Adicionando o primeiro grupo de imagens
        self.add(imagens_1)


        #Animando a câmera
        self.play(
            # Afasta a câmera (multiplica o tamanho do frame por 2.5) e move para o centro entre as duas
            self.camera.frame.animate.scale(2.5).move_to(ORIGIN),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_quad
        )
        
        self.play(
            # Aproxima a câmera de volta (divide por 2.5) e foca na cena da direita
            self.camera.frame.animate.scale(1/2.5).move_to(imagens_1),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_quad
        )

        self.wait(2)


        #Segundo grupo de imagens
        self.play(FadeIn(logo_python.next_to(manim_nome, DOWN, buff=2)))
        self.wait(2)

        #Terceiro grupo de imagens
        self.play(FadeOut(imagens_1), FadeOut(logo_python))

        imagens_3 = Group(Grant_Sanderson, Logo3b1b, b1b_nome, logoytb).arrange(RIGHT, buff=1).shift(RIGHT*7)
        imagens_4 = Group(Logo3b1b, b1b_nome, logoytb)
        logoytb.next_to(b1b_nome, RIGHT, buff=0.1)

        imagens_4.shift(LEFT*3.2)

        Grant_Sanderson.shift(RIGHT*1 + UP*0.5)
        nome_grant.next_to(Grant_Sanderson, DOWN, buff=0.5)


        self.play(FadeIn(imagens_4))
        self.wait(2)
        self.play(Succession(
            imagens_4.animate.scale(0.8).shift(RIGHT*3),
            FadeIn(Grant_Sanderson),
            Write(nome_grant, run_time=1.5)           
        ))

        self.wait(2)
