import socket
import keyboard
import time
import libServo.myLib as xl
import libServo.setData as setData

x = None

host = '127.0.0.1'#thay host cua thiet bi
port = 8000#thay port cua thiet bi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

id142 = '00000142'

def readData():
    data = s.recv(26)#--->13 byte tra ve

    buf = data.hex()
    idMotor = buf[2:10]
    buf_0 = buf[10:12]
    temperature = buf[12:14]

    if idMotor == id142:
        if buf_0 == '30':
            anglePidKp = buf[14:16]
            anglePidKi = buf[16:18]
            speedPidKp = buf[18:20]
            speedPidKi = buf[20:22]
            iqPidKp = buf[22:24]
            iqPidKi = buf[24:]
            xl.readCmd(idMotor).readCmd30(anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi)

        elif buf_0 == '19':
            encoderOffset = buf[22:]
            xl.readCmd(idMotor).readCmd19( encoderOffset)

        elif buf_0 == '9a':
            voltage = buf[16:20]
            xl.readCmd(idMotor).reasCmd9A(temperature, voltage)
            xl.checkState(buf[24:])

        elif buf_0 == 'a3' or buf_0 == 'a4' or buf_0 == 'a5' or buf_0 == 'a6':
            iq = buf[14:18]
            speed = buf[18:22]
            encoder = buf[22:]
            xl.readCmd(idMotor).readCmdA3456(temperature, iq, speed, encoder)

def keyboardServo():
    while True:
        if keyboard.is_pressed('tab'):
            xl.init()

        elif keyboard.is_pressed('space'):
            print("-->Motor stop")
            s.sendall(xl.sendCmd(x,id142).cmdStop())
            time.sleep(0.1)

        elif keyboard.is_pressed('Esc'):
            print("--> Motor off")
            s.sendall(xl.sendCmd(x,id142).cmdOff())
            time.sleep(0.1)

        elif keyboard.is_pressed('F5'):
            s.sendall(xl.sendCmd(x,id142).cmd19())
            time.sleep(0.1)
            readData()

        elif keyboard.is_pressed('c'):
            s.sendall(xl.sendCmd(x,id142).cmd9A())
            time.sleep(0.1)
            readData()

        elif keyboard.is_pressed('right'):#vd
            s.sendall(xl.sendCmd(x,id142).cmdA4(setData.setDT(x).setMaxSpeed(),
                                          setData.setDT(x).setAngleControl()))
            time.sleep(0.1)
            readData()

        elif keyboard.is_pressed('r'):
            s.sendall(xl.sendCmd(x,id142).cmd30())
            time.sleep(0.1)
            readData()

        elif keyboard.is_pressed('w'):
            s.sendall(xl.sendCmd(x,id142).cmd31(setData.setDT(x).setAnglePidKp(),
                                                setData.setDT(x).setAnglePidKi(),
                                                setData.setDT(x).setSpeedPidKp(),
                                                setData.setDT(x).setSpeedPidKi(),
                                                setData.setDT(x).setIqPidKp(),
                                                setData.setDT(x).setIqPidKi()))
            time.sleep(0.1)

        elif keyboard.is_pressed('ctrl + w'):
            s.sendall(xl.sendCmd(x,id142).cmd32(setData.setDT(x).setAnglePidKp(),
                                                setData.setDT(x).setAnglePidKi(),
                                                setData.setDT(x).setSpeedPidKp(),
                                                setData.setDT(x).setSpeedPidKi(),
                                                setData.setDT(x).setIqPidKp(),
                                                setData.setDT(x).setIqPidKi()))
            time.sleep(0.1)


def Main():
    try:
        xl.init()
        keyboardServo()
    finally:
        s.close()

if __name__ == '__main__':
    Main()