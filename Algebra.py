from manim import *

class Algebra(Scene):
    def construct(self):
        # Nombre del archivo
        txt_file = "Algebra.txt"
        
        # Lectura del archivo
        with open(txt_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Extraer LaTeX
        latex_codes = []
        for line in lines:
            line = line.strip()
            if line.startswith("$$") and line.endswith("$$"):
                latex_codes.append(line[2:-2].strip())

        # Configuración de animación
        runtime = 1
        waittime = 1
        last_label = None
        
        # Margen de seguridad (ancho de pantalla menos 1 unidad)
        max_width = config.frame_width - 1.0

        for latex in latex_codes:
            # Crear el objeto matemático
            # Usamos font_size por defecto, luego escalamos si es necesario
            label = MathTex(latex, color=WHITE)
            
            # --- LÓGICA DE ESCALADO AUTOMÁTICO ---
            # Si el ancho del label supera el máximo permitido
            if label.width > max_width:
                # Escala el objeto para que quepa exactamente en el ancho máximo
                label.scale_to_fit_width(max_width)
            # -------------------------------------

            label.move_to(ORIGIN)

            if last_label is None:
                self.play(Write(label), run_time=runtime)
                self.wait(waittime)
            else:
                self.play(ReplacementTransform(last_label, label), run_time=runtime)
                self.wait(waittime)
            
            last_label = label

        if last_label is not None:
            self.wait(0.5)
            self.play(FadeOut(last_label), run_time=0.5)