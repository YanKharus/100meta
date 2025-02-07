import mss
import os
from PIL import Image
import pyautogui
import time
""" time to build up the main loop, my excuse for doing it on main with hardcoded values is because theres like 5x
more things going on than in the tag line full loop which took exactly 1 hour to make"""


def refresh(): # apparently no refresh button anymore guess we'll see
    refreshBoxX = 450
    refreshBoxY = 450
    firstLineInLeaderBoardX = 700
    firstLineInLeaderBoardY = 600  #TODO find real values. theres not even a refresh button anymore lol?

    pyautogui.moveTo(refreshBoxX, refreshBoxY, 1) 
    pyautogui.click()

    pyautogui.moveTo(firstLineInLeaderBoardX, firstLineInLeaderBoardY, 1) 
    pyautogui.click()

def ss(tempFilePath='./temp.png', isFinal=False ) -> None:
    time.sleep(0.5)
    regularCoords = {"top": 380, "left": 190, "width": 720, "height": 500}
    finalCoords = {"top": 745, "left": 190, "width": 720, "height": 162}

    if (isFinal == False):

        with mss.mss() as sct:                     
            sct_img = sct.grab(regularCoords)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=tempFilePath) 
    else: 
         with mss.mss() as sct:
            sct_img = sct.grab(finalCoords)
            mss.tools.to_png(sct_img.rgb, sct_img.size, level=9, output=tempFilePath)


def line1BufferFiller(mainImage='./temp.png', bufferFiller='./images/line-1-filler-test.png', isFinal=False):
    bufferPosX = 125
    bufferPosY = 55
    finalSSPositionX = 125
    finalSSPositionY = 13
    debug = False               #TODO test if all changes and all functions work together wholesale on like 50 tests
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

    mainImage.save('./temp.png')




"""for i in os.listdir('./2-6 tests'):
    line1BufferFiller(f'./2-6 tests/{i}')"""