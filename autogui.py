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





def fullTagLineLoop():
    def tagGet(namesToGet):
        debug = 5 # set to 1 for normal speed or longer for slower
        for i in range(namesToGet): 
            pyautogui.moveTo(500, (i*50) + (400 if namesToGet == 11 else 800), duration=debug) # when getting last 4 names this will move the mouse    
            pyautogui.click(button='right')                                    # to get them
            pyautogui.move(30, 50, duration=debug) # relative movement
            pyautogui.click()
            pyautogui.moveTo(200, 500, duration=debug)
            pyautogui.click()

            clipboard_content = tkinter.Tk().clipboard_get()
            with open('./names.txt', 'a') as nameFile:
                nameFile.write(clipboard_content)

            pyautogui.moveTo(600, 250, duration=debug)
            pyautogui.click()
        
    for i in range(8):
        tagGet(10) 
    else:   # 11 names and 4 names
        tagGet(3)


fullTagLineLoop()