import os
import subprocess
import re
from PIL import Image, ImageEnhance


def png_to_pbm(png_path, pbm_path):
    image = Image.open(png_path)
    image = ImageEnhance.Contrast(image).enhance(5.0)
    image = ImageEnhance.Sharpness(image).enhance(5.0) 
    image = image.convert('1')  # Convert image to black and white
    image.save(pbm_path)
    

def pbm_to_eps(pbm_path):
    subprocess.run(['potrace', f'{pbm_path}'])

def extend_images(dir_path, scale_factor=1.5):
    # Get list of PNG files in directory
    png_files = [f for f in os.listdir(dir_path) if f.startswith('Screen' or 'Problem') and f.endswith('.png')]

    # Find the maximum width among all images
    max_width = max(Image.open(os.path.join(dir_path, f)).size[0] for f in png_files)

    # Extend each image to the maximum width
    for file_name in png_files:
        image = Image.open(os.path.join(dir_path, file_name))
        if image.size[0] < max_width:
            new_image = Image.new('RGB', (max_width, image.size[1]), 'white')
            new_image.paste(image, (0, 0))
            new_image = ImageEnhance.Contrast(new_image).enhance(2.0)
            new_image = ImageEnhance.Sharpness(new_image).enhance(2.0)
            new_image.save(os.path.join(dir_path, file_name))
            
        image = Image.open(os.path.join(dir_path, file_name))
        new_size = tuple([int(dim * scale_factor) for dim in image.size])
        image = image.resize(new_size, Image.ANTIALIAS)
        image.save(os.path.join(dir_path, file_name))



def change_screen_shoot_location(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    command = f'defaults write com.apple.screencapture location {dir_path}/ && defaults write com.apple.screencapture include-date -bool false && defaults write com.apple.screencapture name "Screen Shot" && defaults write com.apple.screencapture include-counter -bool true && killall SystemUIServer'
    print(command)
    subprocess.run(command, shell=True)
    
def rename_screen_shoots(dir_path):
    png_files = [f for f in os.listdir(dir_path) if f.startswith('Screen') and f.endswith('.png')]

    # Extract the integer part from the filename and sort the files based on it
    png_files.sort(key=lambda f: int(re.search(r'\d+', f).group()) if re.search(r'\d+', f) else 0)

    print(png_files)
    for index, file_name in enumerate(png_files, start=1):
        os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, f'Problem_{index}.png'))
        print(f'{file_name} renamed to {index}.png')

    return len(png_files)



def rename_png_to_eps(dir_path):
    # Get list of PNG files in directory
    png_files = [f for f in os.listdir(dir_path) if f.endswith('.png')]

    # Convert each PNG file to EPS
    for png_file in png_files:
        png_path = os.path.join(dir_path, png_file)
        pbm_path = os.path.join(dir_path, os.path.splitext(png_file)[0] + '.pbm')
        #eps_path = os.path.join(dir_path, os.path.splitext(png_file)[0] + '.eps')
        png_to_pbm(png_path, pbm_path)
        pbm_to_eps(pbm_path)

            
def create_main_tex_file(dir_path, title, pngs, eps):
    preamble = r"""\documentclass{article}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\usepackage{geometry}
\usepackage{tasks}
\geometry{
    a4paper,
    left=15mm,
    right=25mm,
    top=10mm,
    bottom=15mm,
    }
"""
    title_format = r"""
\title{Plant Morphology}
\begin{document}
\maketitle
"""
    name_format = r"\includegraphics[width=\textwidth, valign=t]{index.png}"
    with open(f'{dir_path}/main.tex', 'w') as f:
        f.write(preamble)
        f.write(f'{title_format.replace("Plant Morphology", title)}')
        f.write(r'\begin{enumerate}')
        
        for index in range(1, pngs+1):
            f.write(f'\n\t\item')
            if eps:
                f.write(f' {name_format.replace("index", "Problem_" + str(index)).replace(".png", ".eps")}')
            else:
                f.write(f' {name_format.replace("index", "Problem_" + str(index))}')
        
        f.write(f'\n')     
        f.write(r'\end{enumerate}')
        f.write(f'\n')
        f.write(r'\end{document}')
                


def render_to_pdf(dir_path):
    os.chdir(dir_path)
    subprocess.run(['pdflatex', 'main.tex'])
   
   
def back_to_normal():
    subprocess.run('defaults write com.apple.screencapture location ~/Desktop/', shell=True)
    subprocess.run('killall SystemUIServer', shell=True) 
        
        