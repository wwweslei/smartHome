from serial import Serial
from glob import glob


def send(men):
    try:
        ser = Serial(glob('/dev/ttyUSB*')[0], 9600)
        ser.write(str.encode(men))
    except IndexError:
        pass


def teste_usb():
    try:
        return Serial(glob('/dev/ttyUSB*')[0], 9600).name
    except IndexError:
        return "DESCONECTADO"
