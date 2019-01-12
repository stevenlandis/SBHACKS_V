import serial

ard = serial.Serial('/dev/tty96B0', 9600)

if __name__ == '__main__':
    print('Starting')
    while True:
        print(ard.readline())
