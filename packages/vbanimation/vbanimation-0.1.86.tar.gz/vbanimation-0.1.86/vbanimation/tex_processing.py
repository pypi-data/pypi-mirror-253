import os
import re
import subprocess

def solution_to_tikz(file_sol="solution.tex", file_tikz="tikzpicture.tex"):
    """
    Convert the solution in LaTeX format to a TikZ picture.

    Args:
        file_sol (str): Path to the solution file in LaTeX format. Default is "solution.tex".
        file_tikz (str): Path to the TikZ picture file. Default is "tikzpicture.tex".

    Returns:
        str: Path to the generated TikZ picture in PNG format.

    Raises:
        FileNotFoundError: If the solution file or the TikZ picture file is not found.
    """
    with open(file_sol, 'r') as file:
        files = ""
        for i in file:
            files += i
            
        tikz = re.findall(r'\\begin{tikzpicture}.*?\\end{tikzpicture}', files, re.DOTALL)
        
        if tikz:
            tikzpicture = tikz[0]
        else:
            if os.path.exists(file_tikz):
                try:
                    tikzpicture = open(file_tikz, "r").read()
                except FileNotFoundError:
                    raise FileNotFoundError("Solution file or TikZ picture file not found.")
            else:
                return None
        
        if tikzpicture:
            if not os.path.exists("picture"):
                os.mkdir("picture")
        
            with open("picture/tikz.tex", "w") as tikz_file:
                tikz_file.write(tikzpicture)
                
            with open("picture/main.tex", "w") as main_file:
                main_file.write(r"""
                \documentclass[preview, margin=5mm]{standalone}
                \usepackage{v-test-paper}
                \begin{document}
                \color{black}
                \input{tikz.tex}
                \end{document}
                """)
            
            try:
                os.chdir("picture")
                subprocess.call(["pdflatex", "main.tex"])
                subprocess.call(['vbpdf', 'topng', '-t', '-d' , '480'])
                os.chdir("..")
                return 'picture/main.png'
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None
        
        else:
            return None
            
        
def solution_to_align(file_sol="solution.tex"):
    """
    Extract equations from the solution in LaTeX format and organize them into sets.

    Args:
        file_sol (str): Path to the solution file in LaTeX format. Default is "solution.tex".

    Returns:
        dict: A dictionary containing sets of equations.

    Raises:
        FileNotFoundError: If the solution file is not found.
    """
    try:
        with open(file_sol, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Solution file not found.")

    align_matches = re.findall(r'\\begin{align\*}.*?\\end{align\*}', content, re.DOTALL)
    with open("align.tex", "w") as al:
            al.write(align_matches[0])

    with open("align.tex", "r") as f:
        lines = f.readlines()

    equations = []
    for i, line in enumerate(lines):
        intertext_match = re.search(r'\\intertext{.*?}$', line)
        if intertext_match:
            equations.append((intertext_match.group(0), i))
        else:
            equations.append(line.strip())

    dict_equations = {}
    intertext_list = [eq for eq in equations if isinstance(eq, tuple)]

    for i in range(len(intertext_list)):
        start_line = intertext_list[i][1]
        end_line = len(equations) - 1 if i == len(intertext_list) - 1 else intertext_list[i + 1][1]
        dict_equations[f'set_{i+1}'] = [eq[0] if isinstance(eq, tuple) else eq for eq in equations[start_line:end_line]]

    return dict_equations
