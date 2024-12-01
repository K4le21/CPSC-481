from pynput.keyboard import Key, Controller
#import cv2

# Initialize the Controller instance
kb = Controller()

def moveLeft():
    kb.press(Key.left)
    kb.release(Key.left)

def moveRight():
    kb.press(Key.right)
    kb.release(Key.right)