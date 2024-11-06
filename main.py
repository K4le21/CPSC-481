from pynput.keyboard import Key, Controller


def moveLeft(button):
    kb.press(button)
    kb.release(button)

moveLeft(Key.left)