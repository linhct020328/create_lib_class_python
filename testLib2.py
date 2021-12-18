#class
import time

data = None

cmd = None
buf = None
idMotor = '00000142'

anglePidKp = None
anglePidKi = None
speedPidKp = None
speedPidKi = None
iqPidKp = None
iqPidKi = None

spinDirection = None
maxSpeed = None
angleControl = None

flag_check = True

class intTo:
    def __init__(self, x):
        self.x = x

    def hex_8(self):
        return self.x.to_bytes(1, byteorder='big').hex()

    def hex_16(self):
        return self.x.to_bytes(2, byteorder='little').hex()

    def hex_32(self):
        return self.x.to_bytes(4, byteorder='little').hex()

class hexTo:
    def __init__(self, x):
        self.x = x

    def int_8(self):
        self.x = bytes.fromhex(self.x)
        return int.from_bytes(self.x, byteorder="big")

    def int_16(self):
        self.x = bytes.fromhex(self.x)
        return int.from_bytes(self.x, byteorder="little")

    def int_32(self):
        self.x = bytes.fromhex(self.x)
        return int.from_bytes(self.x, byteorder="little")

class setDT:
    def __init__(self, data):
        self.data = data

    def setMaxSpeed(self):
        print("Enter the maxspeed control(<150):")
        self.data = int(input())
        return self.data

    def setAngleControl(self):
        print("Enter the angle control: ")
        self.data = int(input())
        self.data = self.data * 700
        return self.data

    def setAnglePidKp(self):
        print("Enter the angle PID Kp: ")
        self.data = int(input())
        return self.data

    def setAnglePidKi(self):
        print("Enter the angle PID Ki: ")
        self.data = int(input())
        return self.data

    def setSpeedPidKp(self):
        print("Enter the speed PID Kp: ")
        self.data = int(input())
        return self.data

    def setSpeedPidKi(self):
        print("Enter the speed PID Kp: ")
        self.data = int(input())
        return self.data

    def setIqPidKp(self):
        print("Enter the IQ PID Kp: ")
        self.data = int(input())
        return self.data

    def setIqPidKi(self):
        print("Enter the IQ PID Ki: ")
        self.data = int(input())
        return self.data

class sendCmd:
    def __init__(self,cmd):
        self.cmd = cmd

    def cmd30(self, idMotor):
        self.cmd = '08{}3000000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmd31(self, idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        self.cmd = '08{}3100{}{}{}{}{}{}'
        self.cmd = self.cmd.format(idMotor,
                            intTo(anglePidKp).hex_8(),
                            intTo(anglePidKi).hex_8(),
                            intTo(speedPidKp).hex_8(),
                            intTo(speedPidKi).hex_8(),
                            intTo(iqPidKp).hex_8(),
                            intTo(iqPidKi).hex_8())
        return bytes.fromhex(self.cmd)

    def cmd32(self, idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        self.cmd = '08{}3200{}{}{}{}{}{}'
        self.cmd = self.cmd.format(idMotor,
                            intTo(anglePidKp).hex_8(),
                            intTo(anglePidKi).hex_8(),
                            intTo(speedPidKp).hex_8(),
                            intTo(speedPidKi).hex_8(),
                            intTo(iqPidKp).hex_8(),
                            intTo(iqPidKi).hex_8())
        return bytes.fromhex(self.cmd)

    def cmd19(self, idMotor):
        self.cmd = '08{}1900000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmd9A(self, idMotor):
        self.cmd = '08{}9A00000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmdOff(self, idMotor):
        self.cmd = '08{}8000000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmdStop(self, idMotor):
        self.cmd = '08{}8100000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmdRun(self, idMotor):
        self.cmd = '08{}8800000000000000'
        self.cmd = self.cmd.format(idMotor)
        return bytes.fromhex(self.cmd)

    def cmdA3(self, idMotor, angleControl):
        self.cmd = '08{}A3000000{}'
        self.cmd = self.cmd.format(idMotor,
                                   intTo(angleControl).hex_32())
        return bytes.fromhex(self.cmd)

    def cmdA4(self, idMotor, maxSpeed, angleControl):
        self.cmd = '08{}A400{}{}'
        self.cmd = self.cmd.format(idMotor,
                                   intTo(maxSpeed).hex_16(),
                                   intTo(angleControl).hex_32())
        return bytes.fromhex(self.cmd)

    def cmdA5(self, idMotor, spinDirection, angleControl):
        self.cmd = '08{}A5{}0000{}0000'
        self.cmd = self.cmd.format(idMotor,
                                   intTo(spinDirection).hex_8(),
                                   intTo(angleControl).hex_16())
        return bytes.fromhex(self.cmd)

    def cmdA6(self, idMotor, spinDirection, maxSpeed, angleControl):
        self.cmd = '08{}A6{}{}{}0000'
        self.cmd = self.cmd.format(idMotor,
                                   intTo(spinDirection).hex_8(),
                                   intTo(maxSpeed).hex_16(),
                                   intTo(angleControl).hex_16())
        return bytes.fromhex(self.cmd)

class readCmd:
    def __init__(self,buf):
        self.buf = buf

    def readCmd30(self, idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        print('\n----------Return value of cmd 30----------')
        print('id: \t\t\t', idMotor)
        print('anglePidKp: \t', hexTo(anglePidKp).int_8())
        print('anglePidKi: \t', hexTo(anglePidKi).int_8())
        print('speedPidKp: \t', hexTo(speedPidKp).int_8())
        print('speedPidKi: \t', hexTo(speedPidKi).int_8())
        print('iqPidKp: \t\t', hexTo(iqPidKp).int_8())
        print('iqPidKi: \t\t', hexTo(iqPidKi).int_8())

    def readCmd19(self, idMotor, encoderOffset):
        print('\n----------Return value of cmd 19----------')
        print('id: \t\t\t', idMotor)
        print('encoderOffset: \t', hexTo(encoderOffset).int_16())

    def reasCmd9A(self, idMotor, temperature, voltage):
        print('\n----------Return value of cmd 9A----------')
        print('id: \t\t\t', idMotor)
        print('temperature: \t', hexTo(temperature).int_8())
        print('voltage: \t\t', hexTo(voltage).int_16() / 10)

    def readCmdA3456(self, idMotor, temperature, iq, speed, encoder):
        print('\n----------Return value of cmd control----------')
        print('id: \t\t\t', idMotor)
        print('temperature: \t', hexTo(temperature).int_8())
        print('iq: \t\t\t', hexTo(iq).int_16())
        print('speed: \t\t\t', hexTo(speed).int_16())
        print('encoder: \t\t', hexTo(encoder).int_16())

class checkState:
    def __init__(self, endFrame):
        self.endFrame = endFrame
        global flag_check

        if self.endFrame == '00':
            flag_check = False
            print('\n-----> status Normal')

        elif self.endFrame == '01':
            flag_check = True
            print('\n-----> Low voltage protection')

        elif self.endFrame == '10':
            flag_check = True
            print('\n-----> Over temperature protection')

        elif self.endFrame == '11':
            flag_check = True
            print('\n-----> Low voltage protection & over temperature protection')

        while flag_check == True:
            sendCmd(cmd).cmdOff(idMotor)
            print('check Device\n')
            time.sleep(1)

class init:
    def __init__(self):
        print('---------------Select keyboard to execute----------------------')
        print('"tab":\t\tSelect keyboard to execute')
        print('"c":\t\tRead motor status 1 and error flag command')
        print('"F5":\t\tWrite current position to ROM as motor zero commad')
        print('"space":\tMotor stop command')
        print('"Esc":\t\tMotor off command')
        print('"right":\tPosition closed-loop command 2')
        print('"r":\t\tRead PID data command')
        print('"w":\t\tWrite PID to RAM command ')
        print('"ctrl + w":\tWrite PID to ROM command')
        print('--------------------------------------------------------------\n')

