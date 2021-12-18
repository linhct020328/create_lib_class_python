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