import argparse
import time
from random import choice, randint
import logging

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(levelname)-5s] [%(name)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


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


def run_keyboard():
    """
    Performs a random key stroke based on random.choice which is a Uniform distribution
    :return: None
    """
    keyboard = KeyboardController()
    choices = [Key.shift, Key.up, Key.down, Key.left, Key.right, Key.caps_lock, Key.ctrl]

    key_stroke = choice(choices)

    keyboard.press(key_stroke)
    keyboard.release(key_stroke)
    logging.info(f'Pressed {str(key_stroke).split(".")[1]}')


def move_mouse():
    """
    :return: None, moves the mouse relative to current position
    """
    mouse = MouseController()

    # choose random x and y position to move mouse to
    x = randint(-30, 30)
    y = randint(-30, 30)

    mouse.move(x, y)
    logging.info(f'Moved mouse relative to current position {x, y}')


def do_key_stroke(min_time, max_time):
    """
    Main function which executes the keyboard strokes or mouse movement
    :param min_time: lower boundary of time interval
    :param max_time: upper boundary of time interval
    :return: None
    """
    while True:
        t_interval = randint(min_time, max_time)
        which_half = calculate_which_half(min_time, max_time, t_interval)

        if which_half:
            run_keyboard()
        else:
            move_mouse()

        logging.info(f'Waiting {t_interval} seconds')
        time.sleep(t_interval)


def getargs(argv=None):
    parser = argparse.ArgumentParser(description='Process the time interval')
    parser.add_argument(
        "--min_time",
        dest="min_time",
        type=int,
        help="lower boundary of time interval",
    )
    parser.add_argument(
        "--max_time",
        dest="max_time",
        type=int,
        help="upper boundary of time interval",
    )

    return parser.parse_args(argv)


def do_keyboard(min_time=None, max_time=None):
    arg_vals = None
    args = getargs(arg_vals)
    if not min_time:
        min_time = args.min_time
    if not max_time:
        max_time = args.max_time
    logging.info('keyboard.py is running, to stop this script, press CTRL + C')
    print('keyboard.py is running, to stop this script, press CTRL + C')
    do_key_stroke(min_time, max_time)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d [%(levelname)-5s] [%(name)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )
    do_keyboard()
