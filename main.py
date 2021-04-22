import pyautogui as cor
import turtle as pen
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        x, y = cor.position()
        print(x, y)
        pen.goto(x-969, -y+575)
        print(cor.position())


with Listener(on_click=on_click) as listener:
    listener.join()
