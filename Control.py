import DS1X31
import PID
import Thermostat
import os

# Basic Class to wrap irsend
class IrSend:
    def send(self, command):
        return os.system("irsend SEND_ONCE AirCondition " + command)

# Create remote we can use to send commands 
remote = IrSend()

# Create DS1X31 connection, and start conversions
act_temp = DS1X31.DS1X31(0x48)
act_temp.init()
act_temp.start()

print act_temp.getTemp()
