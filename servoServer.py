import socket
import datetime

host = '127.0.0.1'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
client, addr = s.accept()

timeNow = datetime.datetime.now()

def readCmd(buf_0):
    if buf_0 == '30':
        print('-----> Read PID data command')
        data30 = '08 00 00 01 42 30 00 0F 00 05 00 10 00'
        client.sendall(bytes.fromhex(data30))

    elif buf_0 == '31':
        print('-----> Write PID to RAM commannd')
        data31 = '08 00 00 01 42 31 00 0F 00 05 00 10 00'
        client.sendall(bytes.fromhex(data31))

    elif buf_0 == '32':
        print('-----> Write PID to ROM command ')

    elif buf_0 == '19':
        print('-----> Write current position to ROM as motor zero commad')
        data19 = '08 00 00 01 42 19 00 00 00 00 00 00 01'
        client.sendall(bytes.fromhex(data19))

    elif buf_0 == '9a':
        print('-----> Read motor status 1 and error flag commands')
        data9a = '08 00 00 01 42 9A 14 00 28 00 00 00 00'
        client.sendall(bytes.fromhex(data9a))

    elif buf_0 == '81':
        print('-----> Motor stop command')

    elif buf_0 == '88':
        print('-----> Motor running command')
        limitSwitch = '08 00 00 01 42 00 00 00 00 00 00 00 01'
        client.sendall(bytes.fromhex(limitSwitch))

    elif buf_0 == 'a3':
        print('-----> Position closed-loop command 1')
        dataA3 = '08 00 00 01 42 A3 19 E8 03 64 00 E8 03'
        client.sendall(bytes.fromhex(dataA3))

    elif buf_0 == 'a4':
        print('-----> Position closed-loop command 2')
        dataA4 = '08 00 00 01 42 A4 19 E8 03 64 00 E8 03'
        client.sendall(bytes.fromhex(dataA4))

    elif buf_0 == 'a5':
        print('-----> Position closed-loop command 3')
        dataA5 = '08 00 00 01 42 A5 19 E8 03 64 00 E8 03'
        client.sendall(bytes.fromhex(dataA5))

    elif buf_0 == 'a6':
        print('-----> Position closed-loop command 4')
        dataA6 = '08 00 00 01 42 A6 19 E8 03 64 00 E8 03'
        client.sendall(bytes.fromhex(dataA6))

def Main():
    with client:
        try:
            while True:
                data = client.recv(26)
                buf = data.hex()

                idMotor = buf[2:10]
                buf_0 = buf[10:12]
                bufCmd = buf[10:]

                if idMotor == '00000142':
                    print('')
                    print(timeNow, '=> Server respone|', 'ID:', idMotor, '| Command:', bufCmd)
                    readCmd(buf_0)

                if not data:
                    break

        finally:
            client.close()
    s.close()

if __name__ == '__main__':
    Main()