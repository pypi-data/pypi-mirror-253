import click
from .animation_processing import copy_animation
from .animation import EquationAnimation

bg_path = "/Users/vaibhavblayer/10xphysics/backgrounds/bg_instagram.jpg"

@click.command(
        help="Converts pdf pages into pngs"
        )
@click.option(
        '-i',
        '--inputfile',
        type=click.Path(),
        default="./solution.tex",
        show_default=True,
        help="Input file name"
        )
@click.option(
        '-t',
        '--tikzfile',
        type=click.Path(),
        default="./tikzpicture.tex",
        show_default=True,
        help="Tikzpicture file name"
        )
@click.option(
        '-b',
        '--background',
        type=click.Path(),
        default=bg_path,
        show_default=True,
        help="Path of the background image"
        )
@click.option(
        '-p',
        '--pixel_height',
        type=int,
        default=1600,
        show_default=True,
        help="Pixel height of the video"
        )
@click.option(
        '-w',
        '--pixel_width',
        type=int,
        default=1600,
        show_default=True,
        help="Pixel width of the video"
        )
@click.option(
        '-f',
        '--frame_rate',
        type=int,
        default=120,
        show_default=True,
        help="Frame rate of the video"
        )
@click.option(
        '--frame_height',
        type=int,
        default=16,
        show_default=True,
        help="Frame height of the video"
        )
@click.option(
        '--frame_width',
        type=int,
        default=16,
        show_default=True,
        help="Frame width of the video"
        )
@click.option(
        '--st',
        type=float,
        default=0.65,
        show_default=True,
        help="Start time of the video"
        )
@click.option(
        '--se',
        type=float,
        default=0.8,
        show_default=True,
        help="End time of the video"
        )
@click.option(
        '--copy',
        type=bool,
        default=True,
        show_default=True,
        help="Copy Animation after rendering"
        )
@click.option(
        '--trim',
        type=int,
        default=50,
        show_default=True,
        help="Trimming duration of the video"
        )
def main(inputfile, tikzfile, background, pixel_height, pixel_width, frame_rate, frame_height, frame_width, st, se, copy, trim):
        
        if copy:
                EquationAnimation(
                        file_sol=inputfile, 
                        file_tikz=tikzfile, 
                        ph=pixel_height, 
                        pw=pixel_width,
                        fr=frame_rate,
                        fh=frame_height,
                        fw=frame_width,
                        ST=st,
                        SE=se).render()
        
        
                copy_animation(pixel_height, frame_rate, bg_path=background, trim=trim)
                
        else:
                copy_animation(pixel_height, frame_rate, bg_path=background, trim=trim)
    