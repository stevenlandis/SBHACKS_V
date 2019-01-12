import keyboard as key

def Sleep_Mode():
    key.Keyboard.keyDown(key.Keyboard.VK_SLEEP)
    key.Keyboard.keyUp(key.Keyboard.VK_SLEEP)

def Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)

def Shift_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)

def Enter():
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
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_ALT)

def Alt_Shift_Tab():
    key.Keyboard.keyDown(key.Keyboard.VK_SHIFT)
    key.Keyboard.keyDown(key.Keyboard.VK_ALT)
    key.Keyboard.keyDown(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_TAB)
    key.Keyboard.keyUp(key.Keyboard.VK_ALT)
    key.Keyboard.keyUp(key.Keyboard.VK_SHIFT)