from manim import *

class ex01(Scene):
    def construct(self):

        # Criando os objetos da nossa cena
        circulo1 = Circle(radius=3, color=BLUE)
        quadrado1 = Square()
        poligono1 = RegularPolygon(n=5, color=RED)
        ponto = Dot([0,0,0])
        linha = Line(ORIGIN, [0,1,0])

        # Mostrando os efeitos "add" e "remove"
        self.wait()
        self.add(circulo1)
        self.wait()
        self.remove(circulo1)
        self.wait()

        # Mostrando os efeitos "Create" e "Uncreate"
        self.play(Create(quadrado1))
        self.play(Uncreate(quadrado1))
        self.wait()

        # Mostrando os efeitos "FadeIn" e "FadeOut"
        self.play(FadeIn(poligono1))
        self.play(FadeOut(poligono1))
        self.wait()

        # Mostrando o efeito "Transform"
        self.play(Transform(circulo1, poligono1))
        self.wait()

        # Limpando a cena
        self.clear()

        # Mostrando o efeito "ReplacementTransform"
        self.play(ReplacementTransform(ponto, linha))
        self.wait()
