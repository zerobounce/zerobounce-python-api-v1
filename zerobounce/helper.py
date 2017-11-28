
import json
import requests

class ZeroBounceAPI(object):
    def __init__(self, apikey):
        self.apikey = apikey
        self.url = "https://api.zerobounce.net/v1"

    def get_credits(self):
        return int(requests.get("%s/%s" % (self.url, "getcredits"), params={"apikey": self.apikey}).json()["Credits"])

    def validate(self, email):
        return requests.get("%s/%s" % (self.url, "validate"), params={"email": email, "apikey": self.apikey}).json()

    def validatewithip(self, email):
        return requests.get("%s/%s" % (self.url, "validatewithip"), params={"email": email, "apikey": self.apikey, "ipaddress": "99.123.12.122"}).json()
