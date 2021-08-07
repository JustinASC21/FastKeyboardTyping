# imports
import pyautogui as pg
import keyboard
import time
import pytesseract

# url = 'https://www.speedtypingonline.com/typing-tutor'

def screenshot():
    pg.screenshot(region=(350,350,860,120),imageFilename="keybr.png")
    return "keybr.png"
    # returns a PIL image object

def open_web(speed):
    chrome = pg.locateCenterOnScreen("ProjectImages/chrome.png")
    pg.moveTo(chrome)
    pg.click()
    # opens chrome and goes to website
    # after I can perform speed typing program
    url = "https://www.keybr.com/"
    pg.hotkey("ctrl","t")
    # enters the website and goes to online keyboard practice
    pg.typewrite(url,0.1)
    pg.hotkey("enter")

    def pg_speedtype():
        pg.alert("Hold still, our program will get ready...")
        time.sleep(1)
        img = screenshot()
        pg.click(350,350)
        print(speed_typing(img))
        pg.typewrite(speed_typing(img),speed)

    # program ends which means that the speed typer has finished
    # I can ask user if they would like to continue.
    # would ask for the user to remain on the page
    Running = True
    while Running:
        pg_speedtype()
        confirmation = pg.prompt("Would you like to repeat?: ",title="Confirmation")
        confirmation = confirmation.lower()
        if confirmation == "yes" or confirmation == "y":
            pass
        else:
            Running = False


def speed_typing(img):
    '''
   This process will be able to interpret the data such as the keys to type very efficient. I may use screenshot and reading
   text from that screenshot, or may use web scrapping to grab the sentences to type

   For this case scenario as none types are being printed out no matter what website, then span class is not found, so I cant
   grab the letters needed to type
   I can use OpenCV or Pytesseract to read the text from the image
   could add in a speed parameter that lets the user control the speed
   I could also have the program repeat itself based on user input after the words on the screen has been typed out

    :return:_
    '''

    # use Pytesseract to read text from "keybr.png" that has been saved as a file

    # to install the tesseract application to read images in programs folder, we set cmd to this file destination
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\justi\AppData\Local\Programs\Tesseract-OCR\tesseract'

    # this text is the string that is a result from reading the screenshot of the keyboard
    text = pytesseract.image_to_string(img)
    return text
    # after using application file location to work py tesseract, we can read text from an image accurately.


open_web(0.0001)