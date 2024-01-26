import subprocess
import shutil
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from sympy import *

def copy_animation(frame_height, fps, bg_path, trim=50):
    source_file = f'./media/videos/{int(frame_height)}p{int(fps)}/EquationAnimation.mp4'
    
    if not os.path.exists(source_file):
        C = f'ffmpeg -i {bg_path} -i ./media/videos/{int(frame_height)}p{int(fps)}/EquationAnimation.mov  -r {fps} -filter_complex "[0:v][1:v] overlay=0:0" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p ./media/videos/{int(frame_height)}p{int(fps)}/EquationAnimation.mp4'
        subprocess.call(C, shell=True)
    
    
    destination_file = "./downloads/EquationAnimation.mp4"
    
    video = VideoFileClip(source_file)
    print(f"Video duration: {video.duration} seconds")
    
    if video.duration > 60:
        part_1 = f'ffmpeg -i {source_file} -r {fps} -t {trim} -async 1 -c copy ./downloads/EquationAnimation_first_half.mp4'
        subprocess.call(part_1, shell=True)
        part_2 = f'ffmpeg -i {source_file} -r {fps} -ss 00:00:{trim} -async 1 -c copy ./downloads/EquationAnimation_second_half.mp4'
        
        subprocess.call(part_2, shell=True)
        print("Trimmed and Copied successfully!")
    else:
        if shutil.copy2(source_file, destination_file):
            print("Copied successfully!")
