import smbus
import time

bus = smbus.SMBus(1) # 1 indicates /dev/i2c-1

ADDRESS = 0x48

def getTemp():
        pass

def CtoF(celsius):
        return (celsius * (9.0/5.0)) + 32

def initDevice():
        # Start continous conversion
        bus.write_byte(ADDRESS,0x51)
        return

initDevice()

for x in range(10):
        result = bus.read_i2c_block_data(ADDRESS, 0xAA)
        MSB = result[0]
        LSB = result[1]
        whole = MSB
        frac = (LSB>>4) / 256.0
        out = whole + frac
        print(CtoF(out))
        time.sleep(5)
