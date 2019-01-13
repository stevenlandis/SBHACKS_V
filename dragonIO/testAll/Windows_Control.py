import wmi
import pywin32_system32
import sys
import os

def Change_Brightness(brightness):
    try:
        turnVal = round(brightness / 1023 * 100)
        c = wmi.WMI(namespace='wmi')
        methods = c.WmiMonitorBrightnessMethods()[0]
        print('setting brightness to {}'.format(turnVal))
        methods.WmiSetBrightness(turnVal, 0)
    except Exception as e:
        print(e)

brightState = 'light'

def Toggle_Brightness(brightness):
    if brightness == 0:
        return

    global brightState
    try:
        if brightState == 'dark':
            brightState = 'light'
            Change_Brightness(1023)
        else:
            brightState = 'dark'
            Change_Brightness(0)
    except Exception as e:
        print(e)