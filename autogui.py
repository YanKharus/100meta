import pyautogui
import tkinter

""" at this time responsible for getting player names
how am i going to go about developing this
    I need either standardized positions or to just make up placeholders and just build up the skeleton then worry about
    the actual xy positions later. 
generating file structure
    I guess I can hold all the images on my laptop its only 9 images and a text document a day
    all the actual riot api data will be on a database I think 
    so for now make up a loop that holds all information of each day in a specific day folder and that inside a month folder
    should be fine 
making sure this makes sense when its a scheduled task

"""


def scrollDown12Times():
     pyautogui.moveTo(500, 450, duration=1, tween=pyautogui.easeOutElastic)
     pyautogui.click()
     for i in range(12):
          pyautogui.press('down')



def fullTagLineLoop():
    def tagGet(namesToGet):
        debug = 0.5 # set to 1 for normal speed or longer for slower
        for i in range(namesToGet):
            print(i, namesToGet) 
            pyautogui.moveTo(500, (i*40) + (450 if namesToGet == 12 else 800), duration=debug) # when getting last 4 names this will move the mouse    
            pyautogui.click(button='right')                                    # to get them
            pyautogui.move(30, (50 if (i <= 9) else -50), duration=debug) # menu goes up at limited space
            pyautogui.click()
            pyautogui.moveTo(300, 530, duration=1)
            pyautogui.click()

            clipboard_content = tkinter.Tk().clipboard_get()
            with open('./names.txt', 'a', encoding="utf-8") as nameFile:
                nameFile.write(f"{clipboard_content}\n")

            pyautogui.moveTo(1440, 150, duration=debug)
            pyautogui.click()
        
    for i in range(8):
        tagGet(12) 
        scrollDown12Times()
    else:   # 12 names and 4 names
        tagGet(4)
        scrollDown12Times()


#fullTagLineLoop()