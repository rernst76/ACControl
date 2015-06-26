import Thermostat
import json

with open('AccessToken.json') as data:
    auth = json.load(data)

# Get access token
access_token = auth['access_token']

with open('devices.json') as data:
    devices = json.load(data)

thermostats = devices['thermostats']

# Get first item in thermostats dict, which is our thermostat device_id
device_id = thermostats.keys()[0]

# Get structure id
structure_id = thermostats[device_id]['structure_id']

nest = Thermostat.Thermostat(access_token, structure_id ,device_id)

print nest.getTargetTemp()
print nest.getAwayStatus()
