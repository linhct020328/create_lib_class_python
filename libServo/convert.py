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