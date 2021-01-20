from time import sleep, time
import keyboard
from pyperclip import copy

phrase = str(input("type in your phrase\n"))
copy(phrase)

delay = float(input("type in your delay\n"))


def spam():
    a = time()
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("enter")
    print('spammed:', time() - a, "delay")
    sleep(delay)


keyboard.add_hotkey("esc", spam)
keyboard.wait()
