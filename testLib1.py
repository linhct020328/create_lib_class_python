#module
def intToHex8(x):
    return x.to_bytes(1, byteorder='big').hex()

def intToHex16(x):
    return x.to_bytes(2, byteorder='little').hex()

def intToHex32(x):
    return x.to_bytes(4, byteorder='little').hex()

def hexToInt8(x):
    x = bytes.fromhex(x)
    return int.from_bytes(x, byteorder = "big")

def hexToInt16(x):
    x = bytes.fromhex(x)
    return int.from_bytes(x, byteorder= "little")

def hexToInt32(x):
    x = bytes.fromhex(x)
    return int.from_bytes(x, byteorder= "little")

def setMaxSpeed():
    print("Enter the maxspeed control(<150):")
    maxSpeed = int(input())
    return maxSpeed

def setAngleControl():
    print("Enter the angle control: ")
    angleControl = int(input())
    angle = angleControl * 700
    return angle

def setAnglePidKp():
    print("Enter the angle PID Kp: ")
    anglePidKp = int(input())
    return anglePidKp

def setAnglePidKi():
    print("Enter the angle PID Ki: ")
    anglePidKi = int(input())
    return anglePidKi

def setSpeedPidKp():
    print("Enter the speed PID Kp: ")
    speedPidKp = int(input())
    return speedPidKp

def setSpeedPidKi():
    print("Enter the speed PID Kp: ")
    speedPidKi = int(input())
    return speedPidKi

def setIqPidKp():
    print("Enter the IQ PID Kp: ")
    iqPidKp = int(input())
    return iqPidKp

def setIqPidKi():
    print("Enter the IQ PID Ki: ")
    iqPidKi = int(input())
    return iqPidKi

def cmd30(idMotor):
    cmd = '08{}3000000000000000'
    data30 = cmd.format(idMotor)
    return bytes.fromhex(data30)

def readCmd30(idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
    print('\n----------Return value of cmd 30----------')
    print('id: \t\t\t', idMotor)
    print('anglePidKp: \t', hexToInt8(anglePidKp))
    print('anglePidKi: \t', hexToInt8(anglePidKi))
    print('speedPidKp: \t', hexToInt8(speedPidKp))
    print('speedPidKi: \t', hexToInt8(speedPidKi))
    print('iqPidKp: \t\t', hexToInt8(iqPidKp))
    print('iqPidKi: \t\t', hexToInt8(iqPidKi))

# Write PID to RAM
def cmd31(idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
    cmd = '08{}3100{}{}{}{}{}{}'
    data31 = cmd.format(idMotor, intToHex8(anglePidKp), intToHex8(anglePidKi), intToHex8(speedPidKp), intToHex8(speedPidKi),
                        intToHex8(iqPidKp), intToHex8(iqPidKi))
    return bytes.fromhex(data31)

# Write PID to ROM
def cmd32(idMotor, anglePidKp, anglePidKi, speedPidKp, speedPidKi, iqPidKp, iqPidKi):
    cmd = '08{}3200{}{}{}{}{}{}'
    data32 = cmd.format(idMotor, intToHex8(anglePidKp), intToHex8(anglePidKi), intToHex8(speedPidKp), intToHex8(speedPidKi),
                        intToHex8(iqPidKp), intToHex8(iqPidKi))
    return bytes.fromhex(data32)

def cmd19(idMotor):
    cmd = '08{}1900000000000000'
    data19 = cmd.format(idMotor)
    return bytes.fromhex(data19)

def readCmd19(idMotor, encoderOffset):
    print('\n----------Return value of cmd 19----------')
    print('id: \t\t\t', idMotor)
    print('encoderOffset: \t', hexToInt16(encoderOffset))

def cmd9A(idMotor):
    cmd = '08{}9A00000000000000'
    data9A = cmd.format(idMotor)
    return bytes.fromhex(data9A)

def reasCmd9A(idMotor, temperature, voltage):
    print('\n----------Return value of cmd 9A----------')
    print('id: \t\t\t', idMotor)
    print('temperature: \t', hexToInt8(temperature))
    print('voltage: \t\t', hexToInt16(voltage)/10)

def cmdOff(idMotor):
    cmd = '08{}8000000000000000'
    dataStop = cmd.format(idMotor)
    return bytes.fromhex(dataStop)

def cmdStop(idMotor):
    cmd = '08{}8100000000000000'
    dataStop = cmd.format(idMotor)
    return bytes.fromhex(dataStop)

def cmdRun(idMotor):
    cmd = '08{}8800000000000000'
    dataRun = cmd.format(idMotor)
    return bytes.fromhex(dataRun)

def cmdA3(idMotor, angleControl):
    cmd = '08{}A3000000{}'
    dataA3 = cmd.format(idMotor, intToHex32(angleControl))
    return bytes.fromhex(dataA3)

def cmdA4(idMotor, maxSpeed, angleControl):
    cmd = '08{}A400{}{}'
    dataA4 = cmd.format(idMotor, intToHex16(maxSpeed), intToHex32(angleControl))
    return bytes.fromhex(dataA4)

def cmdA5(idMotor, spinDirection, angleControl):
    cmd = '08{}A5{}0000{}0000'
    dataA5 = cmd.format(idMotor, intToHex8(spinDirection), intToHex16(angleControl))
    return bytes.fromhex(dataA5)

def cmdA6(idMotor, spinDirection, maxSpeed, angleControl):
    cmd = '08{}A6{}{}{}0000'
    dataA6 = cmd.format(idMotor, intToHex8(spinDirection), intToHex16(maxSpeed), intToHex16(angleControl))
    return bytes.fromhex(dataA6)

def readCmdA3456(idMotor, temperature, iq, speed, encoder):
    print('\n----------Return value of cmd control----------')
    print('id: \t\t\t', idMotor)
    print('temperature: \t', hexToInt8(temperature))
    print('iq: \t\t\t', hexToInt16(iq))
    print('speed: \t\t\t', hexToInt16(speed))
    print('encoder: \t\t', hexToInt16(encoder))

def checkState(stateError):
    if stateError == '00':
        print('\n-----> status Normal')
        init()

    elif stateError == '01':
        print('\n-----> Low voltage protection')
        print('Select "Esc" to stop the servo')

    elif stateError == '10':
        print('\n-----> Over temperature protection')
        print('Select "Esc" to stop the servo')

    elif stateError == '11':
        print('\n-----> Low voltage protection & over temperature protection')
        print('Select "Esc" to stop the servo')

def init():
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
