import pytesseract
from PIL import Image


 #psm 6 works just as well as default but essentially seems to be about the same 12 seems dog shit but usable and one other only oem 1 available
 #if further tests reveal accuracy is trash then read through increasing accuracy on some github somewhere and researching some of the
 #1000 config variables that can be changed 

def OCR(folderPath: str, dataOutput, isLoop2=False, imagePath='./temp.png') -> None:  
    if( not isLoop2 ):
        imgData = pytesseract.image_to_string(Image.open(imagePath).convert("L"))

        with open(dataOutput, 'a') as dataFile:    # OCR is responsible for carrying temp to final folder
            dataFile.write(imgData)

        with Image.open(imagePath) as players:     
            players.save(folderPath)
    else:
        


OCR('./images/test.png', './imgdata.txt') 

"""TODO both folderpath where player SS and dataoutput where text output will be saved
 should be handled by pyautogui when it calls OCR because it will also handle folder structure as well as 
 maybe fix loop1 and loop2 logic"""