import requests
from firebase import Firebase

"""
Very basic class to provide getting target temperature and away status
from a nest thermostat.
"""

class Thermostat():

    def __init__(self, auth, structure_id, device_id):
        self.device_id = device_id
        self.structure_id = structure_id
        self.auth = auth
        self.fb_target_temp = Firebase(
                'https://developer-api.nest.com/devices/thermostats/' +
                device_id + '/target_temperature_f', auth_token=auth)
        self.fb_away = Firebase(
                'https://developer-api.nest.com/structures/' +
                structure_id + '/away', auth_token=auth)

    # Method to return the target temp
    def getTargetTemp(self):
        return self.fb_target_temp.get()

    # Method to return the away status
    def getAwayStatus(self):
        return self.fb_away.get()
