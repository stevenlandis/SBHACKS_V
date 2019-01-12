import mraa
print(mraa.getVersion())

touch = mraa.Gpio(33)
touch.dir(mraa.DIR_IN)

pastTouch = False
while True:
    currTouch = touch.read()
    if currTouch != pastTouch:
        if currTouch:
            print('pressed')
        else:
            print('released')
        pastTouch = currTouch
