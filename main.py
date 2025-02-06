import mss
import os.path
from PIL import Image
from pyte import OCR
import pyautogui
REFRESHX = 150
REFRESHY = 150 # coordinates for where the refresh box is this is just a placeholder
BUFFERXPOS = 120
BUFFERYPOS = 40 # coordinates for paste function to paste the buffer thing 
# will need to be changed after deciding what the standardized positions off ss's will be


def refresh(REFRESHX, REFRESHY):
    pyautogui.moveTo(REFRESHX, REFRESHY) #TODO find where coordinates are
    pyautogui.click()

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image: # test function working with 21.png alter the values and standardize 
      w = (im1.size[0] + im2.size[0])
      h = max(im1.size[1], im2.size[1])
      z = Image.new("RGBA", (w, h))      # using PIL stuff to crop out the unneeded part from the image after mss takes the ss
      z.paste(im2)                       
      z.paste(im1, (im2.size[0], 0))     

      return z
# no longer being used
def noiseCrop(tempImagePath='./temp.png') -> None:
    try:
        with Image.open(tempImagePath) as z:
                print(z.size)
                debug = False             
                region1 = (0, 0, 60, 355)
                region2 = (400, 0, 589, 355)    # these values are closer to correct
                im1 = z.crop(region2)
                im2 = z.crop(region1)
                result = merge(im1, im2)         # this picks up the temp image saved by ss crops it and overwrites temp 

                if(debug):
                    merge(im1, im2).show()
                    return

                result.save('./images/croptest.png') # OCR picks it up from here does what it needs and OCR will save to actual folder
    except OSError:
            print("something went wrong")
# no longer being used

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

def line1BufferFiller(BUFFERXPOS, BUFFERYPOS, mainImage='./temp.png', bufferFiller='./images/line-1-filler-test.png'):
    debug = False

    mainImage = Image.open(mainImage)
    bufferFiller = Image.open(bufferFiller)

    mainImage.paste(bufferFiller, (BUFFERXPOS, BUFFERYPOS))
    
    if(debug):
        mainImage.show()
        print(mainImage.size)

line1BufferFiller(BUFFERXPOS, BUFFERYPOS)