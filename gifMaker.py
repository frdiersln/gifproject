import glob
from PIL import Image

def make_gif(path, ext):
    frames = [Image.open(image) for image in glob.glob(f"{path}/*.png")]
    frame_one = frames[0]
    frame_one.save(f"{path}/my_awesome.{ext}", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    
make_gif("gif1", "apng")