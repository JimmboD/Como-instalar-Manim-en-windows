from manim import *
import numpy as np

class miniatura(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": WHITE, "stroke_width": 2},
        )

        def calc_field(pos):
            x, y = pos[:2]
            
            if x == 0 and y == 0:
                return np.array([0, 0, 0])
            
            denominator = np.sqrt(x**2 + y**2)
            
            u = -y / denominator
            v = x / denominator
            
            return np.array([u, v, 0])

        vector_field = ArrowVectorField(
            calc_field,
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            color=YELLOW,
            length_func=lambda x: 0.5  # Mantiene el tamaño de las flechas uniforme visualmente
        )

        self.play(Create(axes), run_time=1.5)
        self.play(Create(vector_field), run_time=3)
        self.wait(2)