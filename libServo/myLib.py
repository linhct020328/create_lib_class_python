import libServo.convert as convert
import time

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

class sendCmd:
    def __init__(self,cmd, idMotor):
        self.cmd = cmd
        self.idMotor = idMotor

    def cmd30(self):
        self.cmd = '08{}3000000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmd31(self, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        self.cmd = '08{}3100{}{}{}{}{}{}'
        self.cmd = self.cmd.format(self.idMotor,
                            convert.intTo(anglePidKp).hex_8(),
                            convert.intTo(anglePidKi).hex_8(),
                            convert.intTo(speedPidKp).hex_8(),
                            convert.intTo(speedPidKi).hex_8(),
                            convert.intTo(iqPidKp).hex_8(),
                            convert.intTo(iqPidKi).hex_8())
        return bytes.fromhex(self.cmd)

    def cmd32(self, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        self.cmd = '08{}3200{}{}{}{}{}{}'
        self.cmd = self.cmd.format(self.idMotor,
                            convert.intTo(anglePidKp).hex_8(),
                            convert.intTo(anglePidKi).hex_8(),
                            convert.intTo(speedPidKp).hex_8(),
                            convert.intTo(speedPidKi).hex_8(),
                            convert.intTo(iqPidKp).hex_8(),
                            convert.intTo(iqPidKi).hex_8())
        return bytes.fromhex(self.cmd)

    def cmd19(self):
        self.cmd = '08{}1900000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmd9A(self):
        self.cmd = '08{}9A00000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmdOff(self):
        self.cmd = '08{}8000000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmdStop(self):
        self.cmd = '08{}8100000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmdRun(self):
        self.cmd = '08{}8800000000000000'
        self.cmd = self.cmd.format(self.idMotor)
        return bytes.fromhex(self.cmd)

    def cmdA3(self, angleControl):
        self.cmd = '08{}A3000000{}'
        self.cmd = self.cmd.format(self.idMotor,
                                   convert.intTo(angleControl).hex_32())
        return bytes.fromhex(self.cmd)

    def cmdA4(self, maxSpeed, angleControl):
        self.cmd = '08{}A400{}{}'
        self.cmd = self.cmd.format(self.idMotor,
                                   convert.intTo(maxSpeed).hex_16(),
                                   convert.intTo(angleControl).hex_32())
        return bytes.fromhex(self.cmd)

    def cmdA5(self, spinDirection, angleControl):
        self.cmd = '08{}A5{}0000{}0000'
        self.cmd = self.cmd.format(self.idMotor,
                                   convert.intTo(spinDirection).hex_8(),
                                   convert.intTo(angleControl).hex_16())
        return bytes.fromhex(self.cmd)

    def cmdA6(self, spinDirection, maxSpeed, angleControl):
        self.cmd = '08{}A6{}{}{}0000'
        self.cmd = self.cmd.format(self.idMotor,
                                   convert.intTo(spinDirection).hex_8(),
                                   convert.intTo(maxSpeed).hex_16(),
                                   convert.intTo(angleControl).hex_16())
        return bytes.fromhex(self.cmd)

class readCmd:
    def __init__(self,idMotor):
        self.idMotor = idMotor

    def readCmd30(self, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
        print('\n----------Return value of cmd 30----------')
        print('id: \t\t\t', self.idMotor)
        print('anglePidKp: \t', convert.hexTo(anglePidKp).int_8())
        print('anglePidKi: \t', convert.hexTo(anglePidKi).int_8())
        print('speedPidKp: \t', convert.hexTo(speedPidKp).int_8())
        print('speedPidKi: \t', convert.hexTo(speedPidKi).int_8())
        print('iqPidKp: \t\t', convert.hexTo(iqPidKp).int_8())
        print('iqPidKi: \t\t', convert.hexTo(iqPidKi).int_8())

    def readCmd19(self, encoderOffset):
        print('\n----------Return value of cmd 19----------')
        print('id: \t\t\t', self.idMotor)
        print('encoderOffset: \t', convert.hexTo(encoderOffset).int_16())

    def reasCmd9A(self, temperature, voltage):
        print('\n----------Return value of cmd 9A----------')
        print('id: \t\t\t', self.idMotor)
        print('temperature: \t', convert.hexTo(temperature).int_8())
        print('voltage: \t\t', convert.hexTo(voltage).int_16() / 10)

    def readCmdA3456(self, temperature, iq, speed, encoder):
        print('\n----------Return value of cmd control----------')
        print('id: \t\t\t', self.idMotor)
        print('temperature: \t', convert.hexTo(temperature).int_8())
        print('iq: \t\t\t', convert.hexTo(iq).int_16())
        print('speed: \t\t\t', convert.hexTo(speed).int_16())
        print('encoder: \t\t', convert.hexTo(encoder).int_16())

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


