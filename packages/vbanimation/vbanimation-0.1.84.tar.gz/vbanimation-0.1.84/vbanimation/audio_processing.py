from re import findall, sub
import subprocess
from manim import *
from .other_functions import get_audio_duration
from .tex_parsing import parse_and_transform_maths
import time


def process_tex_to_text(tex_string):
    tex_string = tex_string.replace(r'\intertext{', r'')
    tex_string = tex_string.replace(r'\\[2mm]', r'')
    tex_string = tex_string.replace(r'&', r'')
    tex_string = tex_string.replace(r'\Rightarrow', r'')
    tex_string = tex_string.replace(r'|', '\\|')
    tex_string = sub(r'}\n', '\n', tex_string) 
    math_expressions = findall(r'\$(.*?)\$', tex_string)
    print(math_expressions)
    for i in math_expressions:
        eng_expr = parse_and_transform_maths(f'${i}$')
        tex_string = tex_string.replace(f'${i}$', eng_expr)
        
    
    print(tex_string)
    return tex_string
    
    
def get_audio(text, key):
    print(text)
    try:
        audio_command = f'say -o {key}.aac "{text}" -r 150'
        print(audio_command)
        subprocess.call(audio_command, shell=True) 
        time.sleep(1) 
        duration = get_audio_duration(f'{key}.aac')
        return duration
    except:
        print('Error in getting audio')
        return 0.02*len(text)
    
       



        
        

    
    
        

            


       

        



    