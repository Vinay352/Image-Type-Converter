import glob 
from PIL import Image
import sys
import argparse
i=0
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to the folder which contains the images file")
args = vars(ap.parse_args())
filename=args["input"]
for file in glob.glob(filename+'\*.*'):
    try:
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(str(i)+".jpg")
        i+=1
    except Exception as e:
        print(e)