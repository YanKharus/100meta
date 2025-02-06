import pytesseract
from PIL import Image
import cv2
import os
import subprocess

def invertBlackWhiteImageOnly(Image: Image.Image):
     
    return Image.point(lambda z: 0 if z == 255 else 255)


 #psm 6 works just as well as default but essentially seems to be about the same 12 seems dog shit but usable and one other only oem 1 available
 #if further tests reveal accuracy is trash then read through increasing accuracy on some github somewhere and researching some of the
 #1000 config variables that can be changed 

def OCR(playerRanksPath: str, playerInfoTxt: str,config, stagingRanksPath='./temp.png') -> None:  
        
        img = cv2.imread(stagingRanksPath, cv2.IMREAD_GRAYSCALE)
        _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

        img_pil = Image.fromarray(img)
        
        img_pil = invertBlackWhiteImageOnly(img_pil)

        img_pil.save(f"./images/{len(os.listdir('./images')) +1}.png")

    
        imgData = f"{pytesseract.image_to_string(img_pil, config=config)}\n\n"

        """ when debugging to check what pytesseract is *actually* looking at run this in cli with the 
        pre-processed image because it wont have access to these functions
        tesseract 12.png output --psm 6 -c tessedit_char_whitelist=0123456789/ -c tessedit_write_images=1 """
             
        with open(playerInfoTxt, 'a') as OCRtext:   
            OCRtext.write(imgData)

        with Image.open(stagingRanksPath) as players:      # OCR is responsible for carrying temp to final folder
            players.save(playerRanksPath)


moreconfigs= ["--psm 3 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 4 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 5 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789/",
                  "--psm 12 --oem 3 -c tessedit_char_whitelist=0123456789/"]

config = '--psm 6 -c tessedit_char_whitelist=0123456789/'

"""for i in os.listdir('./2-6 modified tests'):
     OCR('./OCRimagesaving.png', './text.txt', config, stagingRanksPath=f'./2-6 modified tests/{i}')"""


    





