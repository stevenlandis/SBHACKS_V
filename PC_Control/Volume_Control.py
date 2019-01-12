from sound import Sound

def Increase_Volume(amount):
    for i in range(amount):
        Sound.volume_up()

def Decrease_Volume(amount):
    for i in range(amount):
        Sound.volume_down()

def Mute():
    Sound.mute()

def Max_Volume():
    Sound.volume_max()

def Min_Volume():
    Sound.volume_min()

def Get_Volume():
    return Sound.current_volume()
