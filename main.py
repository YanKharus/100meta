import mss
import os
from PIL import Image
import pyautogui


def refresh():
    REFRESHX = 450
    REFRESHY = 450
    pyautogui.moveTo(REFRESHX, REFRESHY, 1) #TODO have it also click the leaderboard so the scrollbar is active
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

def ss(tempFilePath='./temp.png', isFinal=False ) -> None:
    monitor = {"top": 380, "left": 190, "width": 720, "height": 500}
    finalSSCoords = {}

    if (isFinal == False):

        with mss.mss() as sct:                     #TODO test if changes work
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=tempFilePath) 
    else: 
         with mss.mss() as sct:
            sct_img = sct.grab(finalSSCoords)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=tempFilePath)


def line1BufferFiller(mainImage='./temp.png', bufferFiller='./images/line-1-filler-test.png', isFinal=False):
    bufferPosX = 125
    bufferPosY = 55
    finalSSPositionX = 1
    finalSSPositionY = 1
    debug = False               #TODO test if changes work this also needs to return or actually save something
    if (isFinal == False):
        mainImage = Image.open(mainImage)
        bufferFiller = Image.open(bufferFiller)
                        
        mainImage.paste(bufferFiller, (bufferPosX, bufferPosY))
    else:
        mainImage = Image.open(mainImage)
        bufferFiller = Image.open(bufferFiller)
                            
        mainImage.paste(bufferFiller, (finalSSPositionX, finalSSPositionY))

    if(debug):
        mainImage.show()
        print(mainImage.size)

    mainImage.save(f'./2-6 modified tests/{len(os.listdir('./2-6 modified tests'))+1}.png')

def scrollDown12Times():
     for i in range(12):
          pyautogui.press('down')


#line1BufferFiller(BUFFERXPOS, BUFFERYPOS)
#refresh(REFRESHX, REFRESHY)

"""for i in os.listdir('./2-6 tests'):
    line1BufferFiller(f'./2-6 tests/{i}')"""