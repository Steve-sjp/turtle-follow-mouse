import turtle
import turtle as pen
from pynput.mouse import Listener

screen = turtle.Screen()


def on_scroll(x, y, dx, dy):
    if dy > 0:
        print('pen up')
        pen.up()
        pen.write('                      pen up')

    if dy < 0:
        print('pen down')
        pen.down()
        pen.write('                      pen down')


def fxn(x, y):
    pen.setheading(pen.towards(x, y))
    pen.goto(x, y)
    pen.write(str(x) + "," + str(y))
    print("x =", x, ",", "y =", y)


with Listener(on_scroll=on_scroll) as listener:
    screen.onclick(fxn)
    screen.mainloop()
    listener.join()