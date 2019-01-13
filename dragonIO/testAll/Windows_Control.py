import wmi
import pywin32_system32
import sys
import os


def Change_Brightness(brightness):
    turnVal = round(brightness/ 1023 * 100)
    c = wmi.WMI(namespace='wmi')

    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(turnVal, 0)

