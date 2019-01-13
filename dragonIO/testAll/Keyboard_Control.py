import keyboard as key
from time import sleep

def Scroll_Windows(arg):
    if arg == 0:
        Alt_Tab()
    else:
        Alt_Shift_Tab()

def Scroll_Tabs(arg):
    if arg == 0:
        Ctrl_Tab()
    else:
        Ctrl_Shift_Tab()

def Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)

def Shift_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)

def Enter(arg):
    if arg == 0:
        return
    key.Keyboard.keyDown(key.Keyboard.VK_ENTER)
    key.Keyboard.keyUp(key.Keyboard.VK_ENTER)

def Shift():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)

def Ctrl():
    key.Keyboard.keyDown(key.Keyboard.VK_CTRL)
    key.Keyboard.keyUp(key.Keyboard.VK_CTRL)

def BackSpace():
    key.Keyboard.keyDown(key.Keyboard.VK_BACKSPACE)
    key.Keyboard.keyUp(key.Keyboard.VK_BACKSPACE)

def B_Back():
    key.Keyboard.keyDown(key.Keyboard.VK_BROWSER_BACK)
    key.Keyboard.keyUp(key.Keyboard.VK_BROWSER_BACK)

def B_Favorite():
    key.Keyboard.keyDown(key.Keyboard.VK_BROWSER_FAVORITES)
    key.Keyboard.keyUp(key.Keyboard.VK_BROWSER_FAVORITES)

def B_Forward():
    key.Keyboard.keyDown(key.Keyboard.VK_BROWSER_FORWARD)
    key.Keyboard.keyUp(key.Keyboard.VK_BROWSER_FORWARD)


def Alt_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_ALT)
    sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_ALT)

def Alt_Shift_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_ALT)
    sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_ALT)
    sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)

def Ctrl_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_CTRL)
    # sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_CTRL)

def Ctrl_Shift_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    # sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_CTRL)
    # sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_CTRL)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)

def Ctrl_W(arg):
    if arg == 0:
        return
    key.Keyboard.keyDown(key.Keyboard.VK_CTRL)
    # sleep(0.1)
    key.Keyboard.keyDown(key.Keyboard.VK_W)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_W)
    # sleep(0.1)
    key.Keyboard.keyUp(key.Keyboard.VK_CTRL)