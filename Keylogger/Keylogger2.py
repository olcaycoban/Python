from pynput.mouse import Button , Controller
from pynput.keyboard import Controller

def ControlMouse():
    mouse = Controller()
    mouse.position = (10,20)
    print(mouse.position)
def ControlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello World !!! ")
ControlKeyboard()
ControlMouse()

