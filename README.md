# FastKeyboardTyping
This program is more of a fun way to use pyautogui, and with this program the user will be directed to a typing practice website specifically: https://www.keybr.com/  ;  and the computer will type in the letters to the practice interface from the website 

The user interface from the website in which the program will be typing on looks like this

![image](https://user-images.githubusercontent.com/87743966/128600381-43041918-f267-410c-9dab-c15410d76c0f.png)

This program will take a screenshot of this inerface read the image with the pytesseract library and translate it into a string. I even have the program print out the resulting string into the terminal.

![image](https://user-images.githubusercontent.com/87743966/128600421-2218920a-e44b-496a-8e87-ee3fca6f9945.png)

The above snippet is an example of what the program has processed, and will then direct the mouse to the top left corner to click on the online keyboard, and start typing away.

(This program is in its first stages as it relies on the user having a screenshot of chrome, in order to find the web and to open it up. However, I look to be able to open up a web browser without relying on an image.)
