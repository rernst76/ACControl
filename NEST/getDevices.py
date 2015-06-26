import requests
from firebase import Firebase
import json

# Open AccessToken file to load access token for Nest API
with open('AccessToken.json') as json_file:
    data = json.load(json_file)

access_token = data['access_token']
email = 'rernst76@gmail.com'

# create firebase object
fb = Firebase('https://developer-api.nest.com/devices',
        auth_token=access_token)

# get devices 
devices = fb.get()

# dump devises into json file
with open('devices.json', 'w') as json_out:
    json.dump(devices, json_out)

print devices
print "Devices file created!"
