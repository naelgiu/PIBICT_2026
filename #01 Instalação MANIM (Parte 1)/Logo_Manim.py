from manim import *

class Logo_Manim(MovingCameraScene):
    def construct(self):
        mob = ManimBanner()
        
        self.play(Create(mob), run_time=3)
        self.play(self.camera.frame.animate.set(width=mob.width * 1.2).move_to(mob), run_time=10)
