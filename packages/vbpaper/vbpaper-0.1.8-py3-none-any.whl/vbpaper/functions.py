import os
import subprocess


def change_screen_shoot_location(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    command = f'defaults write com.apple.screencapture location {dir_path}/'
    print(command)
    subprocess.run(command, shell=True)
    subprocess.run('killall SystemUIServer', shell=True)
    
    
def rename_screen_shoots(dir_path):
    png_files = [f for f in os.listdir(dir_path) if os.path.splitext(f)[1] == '.png']
    png_files.sort(key=lambda f: os.path.getctime(os.path.join(dir_path, f)))
    print(png_files)
    for index, file_name in enumerate(png_files, start=1):
        os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, f'{index}.png'))
        
            
            
def create_main_tex_file(dir_path, title):
    preamble = r"""\documentclass{article}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\usepackage{geometry}
\usepackage{tasks}
\geometry{
    a4paper,
    total={170mm,257mm},
    left=20mm,
    top=10mm,
    }
"""
    title_format = r"""
\title{Plant Morphology}
\begin{document}
\maketitle
"""
    name_format = r"\includegraphics[width=0.8\textwidth, valign=t]{index.png}"
    with open(f'{dir_path}/main.tex', 'w') as f:
        f.write(preamble)
        f.write(f'{title_format.replace("Plant Morphology", title)}')
        f.write(r'\begin{enumerate}')
        png_files = [f for f in os.listdir(dir_path) if os.path.splitext(f)[1] == '.png']
        png_files.sort(key=lambda f: os.path.getctime(os.path.join(dir_path, f)))
        print(png_files)
        for index, file_name in enumerate(png_files, start=1):
            f.write(f'\n\t\item')
            f.write(f' {name_format.replace("index", str(index))}')
        
        f.write(f'\n')     
        f.write(r'\end{enumerate}')
        f.write(f'\n')
        f.write(r'\end{document}')
                


def render(dir_path):
    os.chdir(dir_path)
    subprocess.run(['pdflatex', 'main.tex'])
   
   
def back_to_normal():
    subprocess.run('defaults write com.apple.screencapture location ~/Desktop/', shell=True)
    subprocess.run('killall SystemUIServer', shell=True) 
        
        