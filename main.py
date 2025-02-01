import mss
import os.path
from PIL import Image
from pyte import OCR

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image: # test function working with 21.png alter the values and standardize 
      w = (im1.size[0] + im2.size[0])
      h = max(im1.size[1], im2.size[1])
      z = Image.new("RGBA", (w, h))      # using PIL stuff to crop out the unneeded part from the image after mss takes the ss
      z.paste(im2)                       # IF YOU ARE USING THIS FUNCTION THAT MEANS YOU SHOULD BE IN LOOP 1
      z.paste(im1, (im2.size[0], 0))     

      return z

def noiseCrop(tempImagePath='./temp.png') -> None:
    try:
        with Image.open(tempImagePath) as z:       
                debug = False                 # IF YOU ARE USING THIS FUNCTION THEN YOU SHOULD BE IN LOOP 1
                region1 = (0, 0, 110, 700)
                region2 = (160, 0, 1000, 700)    # default values most likely need to be changed
                im1 = z.crop(region2)
                im2 = z.crop(region1)
                result = merge(im1, im2)         # this picks up the temp image saved by ss crops it and overwrites temp 

                if(debug):
                    print(merge(im1, im2).show())

                result.save(tempImagePath) # OCR picks it up from here does what it needs and OCR will save to actual folder
    except OSError:
            print("something went wrong")


def ss(folderPath: str, isLoop2: bool, tempFilePath='./temp.png' ) -> None:

 # all this needs to do is save to temp or save to tag folder dump
    with mss.mss() as sct:
        if (not isLoop2):
            monitor = {"top": 380, "left": 150, "width": 1000, "height": 700}

            # Grab the data
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=tempFilePath) 

        else:
            monitor={} #TODO set values for catching the taglines
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=folderPath)  
        #TODO?   most likely leaving this up to wrapper function logic  ^^^^^^^^^^

