import os
import glob
from PIL import Image

def resize(path, xsize, ysize, ext):
    imgs = [Image.open(image) for image in glob.glob(f"{path}/*.{ext}")]

    try:
        os.mkdir(os.path.join(path, "resized"))
    except:
        pass

    for img in imgs:
        resized = img.resize((xsize, ysize))
        resized.save(f"{path}" + "/resized/" + img.filename.split("\\")[1])

resize("gif1", 1440, 720, "png")