import json
from threading import Thread

import requests


class StartupDetailsScraper(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        self.json = 'None'
        self.pitch = 'None'

    def run(self):
        response = requests.get(self.url)
        self.json = response.text

        try:
            data = json.loads(self.json)
            self.pitch = data['details']['pitch']
        except ValueError:
            print response.text

        data = json.loads(self.json)
        self.pitch = data['details']['pitch']

    def clean(self, input):
        if input == None or input == '':
            return 'empty'
        else:
            return input

    def get_json(self):
        return self.clean(self.json)

    def get_pitch(self):
        return self.clean(self.pitch)
