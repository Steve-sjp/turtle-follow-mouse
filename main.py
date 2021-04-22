import pyautogui as cor
import turtle as pen
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        x, y = cor.position()
        print("x =", x, ",", "y =", y)
        pen.goto(x-969, -y+575)


def on_scroll(x, y, dx, dy):
    if dy > 0:
        print('pen up')
        pen.up()

    if dy < 0:
        print('pen down')
        pen.down()


with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
