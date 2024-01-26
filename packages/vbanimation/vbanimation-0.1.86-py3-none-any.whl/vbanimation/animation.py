from manim import *
from .tex_processing import solution_to_align, solution_to_tikz
from .other_functions import chunk_words
from .audio_processing import process_tex_to_text, get_audio

class EquationAnimation(MovingCameraScene):
    bo = 0
    def __init__(self, file_sol, file_tikz, ph, pw, fh, fw, fr, ST, SE, **kwargs):
        self.file_sol = file_sol
        self.file_tikz = file_tikz  
        self.ph = ph
        self.pw = pw
        self.fh = fh
        self.fw = fw
        self.fr = fr
        self.ST = ST
        self.SE = SE
        
        config.pixel_height = ph
        config.pixel_width = pw
        config.frame_height = fh
        config.frame_width = fw
        config.frame_rate = fr
        

        super().__init__(**kwargs)
        
    
    config.background_opacity = bo
    config.movie_file_extension = '.mov'
    def construct(self):
        Tex.set_default(color=BLACK)
        Mobject.set_default(color=BLACK)
		
        H = config.frame_height
        W = config.frame_width
        
        custom_template = TexTemplate()
        custom_template.add_to_preamble(r"\usepackage{v-test-paper}")
        equations = solution_to_align(file_sol=self.file_sol)
        image = solution_to_tikz(file_sol=self.file_sol, file_tikz=self.file_tikz)
        title = Tex(r'\texttt{Solution}', tex_template=custom_template).scale(0.8).to_edge(UP)
        self.add(title)
        
        N = len(equations)
        PL = None
        
        ST = self.ST
        SE = self.SE
        
        if image:
            image = ImageMobject(image)
            if image.height > image.width:
                image.height = 0.5*H
            else:
                image.width = 0.65*W
            PL = image.get_bottom()
            self.play(FadeIn(image))
            self.wait(2)
            N += 1
        else:
            PL = ([0, 0.25*H, 0])
            
        
        for key, value in equations.items():
            
            if len(value) == 1:
                tex_string = value[0].replace(r'\intertext{', r'{$\Rightarrow \quad$')
                tex_string = '\\\\'.join(chunk_words(tex_string, int(W)))
                T = Tex(tex_string, tex_template=custom_template).scale(ST).next_to(([-0.5*W, PL[1] - 1.5, 0]), RIGHT, buff=1)
                
                duration = get_audio(process_tex_to_text(value[0]), key)
                self.add_sound(f'{key}.aac')
                self.play(
                    self.camera.frame.animate.move_to(([0, T.get_y(), 0])),
                    Create(T),
                    run_time=duration
                    #run_time=0.03*len(T.get_tex_string())
                )
                self.wait(0.5)
                PL = T.get_bottom()
            else:
                ML = [i + r'[2mm]' if i.endswith(r'\\') else i for i in value[1:] ]
                tex_string = value[0].replace(r'\intertext{', r'{$\Rightarrow \quad$')
                
                tex_string = '\\\\'.join(chunk_words(tex_string, int(W)))
                T = Tex(tex_string, tex_template=custom_template).scale(ST).next_to(([-0.5*W, PL[1] - 1.5, 0]), RIGHT, buff=1)
                
                PL = T.get_bottom()
                L = MathTex(*ML, tex_template=custom_template).scale(SE).next_to(([0, PL[1], 0]), DOWN, buff=0.5)
                PL = L.get_bottom()
                
                duration = get_audio(process_tex_to_text(value[0]), key)
                self.add_sound(f'{key}.aac')
                self.play(
                    self.camera.frame.animate.move_to(([0, T.get_y(), 0])),
                    Create(T),
                    run_time = duration
                    #run_time=0.05*len(T.get_tex_string())
                )
                
                for i in range(len(L)):
                    duration = get_audio(process_tex_to_text(f'$[[slnc 500]] {L[i].get_tex_string()}$'), f'{key}_{i}')
                    self.add_sound(f'{key}_{i}.aac')
                    self.play(
                        self.camera.frame.animate.move_to(([0, L[i].get_y(), 0])),
                        Create(L[i]),
                        run_time = duration
                        #run_time=0.05*len(L[i].get_tex_string())
                    )
                    self.wait(0.5)
             
            self.wait(1.5)       
            
                    
        
        self.play(self.camera.frame.animate.move_to(ORIGIN))
        self.wait()
        self.play(self.camera.frame.animate.move_to(([0, PL[1], 0])), run_time=2*N, rate_func=linear)
        circle = Circle(color=WHITE, radius=0.1, fill_opacity=1).move_to(([0, PL[1], 0]))
        self.play(
            circle.animate.scale(120)
            )
        self.play(
            Create(Tex(r'\texttt{@10xphysics}', tex_template=custom_template).scale(ST).move_to(([0, PL[1], 0])))
        )
        self.wait(1)
        
        
        