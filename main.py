from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from random import choice, randint
import time


def calculate_which_half(low, high, x):
    """
    :param low: numeric value lower boundary
    :param high: numeric value higher boundary
    :param x: random number drawn between low and high
    :return: boolean
    """

    lower_half = (high - low) / 2 + low

    if x > lower_half:
        return True
    else:
        return False


def run_keyboard(min_time, max_time):
    """
    :param min_time: minimum amount of time interval between keyboard or mouse action
    :param max_time: minimum amount of time interval between keyboard or mouse action
    :return: None
    """
    keyboard = KeyboardController()
    choices = [Key.shift, Key.up, Key.down, Key.left, Key.right, Key.caps_lock,Key.ctrl]

    key_stroke = choice(choices)

    keyboard.press(key_stroke)
    keyboard.release(key_stroke)
    print(f'Pressed {str(key_stroke).split(".")[1]}')


def move_mouse():

    mouse = MouseController()

    # choose random x and y position to move mouse to
    x = randint(-30, 30)
    y = randint(-30, 30)

    mouse.move(x, y)
    print(f'Moved mouse relative to current position {x, y}')


def do_key_stroke(min_time, max_time):

    while True:
        t_interval = randint(min_time, max_time)
        which_half = calculate_which_half(min_time, max_time, t_interval)

        if which_half:
            run_keyboard(min_time, max_time)
        else:
            move_mouse()

        print(f'Waiting {t_interval} seconds')
        time.sleep(t_interval)


if __name__ == '__main__':
    print('keyboard.py is running, to stop this script, press CTRL + C')
    do_key_stroke(0, 20)
