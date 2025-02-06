import mss
import os
from PIL import Image
import pyautogui

def refresh():
    refreshBoxX = 450
    refreshBoxY = 450
    firstLineInLeaderBoardX = 700
    firstLineInLeaderBoardY = 600  #TODO find real values

    pyautogui.moveTo(refreshBoxX, refreshBoxY, 1) 
    pyautogui.click()

    pyautogui.moveTo(firstLineInLeaderBoardX, firstLineInLeaderBoardY, 1) 
    pyautogui.click()

def ss(tempFilePath='./temp.png', isFinal=False ) -> None:
    monitor = {"top": 380, "left": 190, "width": 720, "height": 500}
    finalSSCoords = {}

    if (isFinal == False):

        with mss.mss() as sct:                     #TODO test if changes work and find final box coordinates
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



"""for i in os.listdir('./2-6 tests'):
    line1BufferFiller(f'./2-6 tests/{i}')"""