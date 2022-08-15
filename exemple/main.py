from manim import *

class Main(Scene):
    def construct(self):
        self.camera.background_color = "#252e42"
        cercle = Circle(color=RED).scale(1)
        submark = (Text("First tutorial")
                                        .set_color("#ffe3c8")
                                        .scale(0.5)
                                        .to_edge(UP)
                                        .set_color_by_gradient([PINK, BLUE, RED])
                                                    )
        mob = Dot(radius=2.0).set_color_by_gradient([PINK, BLUE, RED])
        
        self.play(Create(cercle))
        self.play(Write(mob), run_time = 1.4)
        self.play(Transform(cercle, submark), run_time = 1)
        self.wait(2)
    
def main():
    with tempconfig({"preview":True, "format":"gif"}):
        scene = Main()
        scene.render()
    
if __name__ == '__main__':
    main()
    