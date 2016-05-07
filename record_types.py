class TechInAsiaRecord:
    def __init__(self):
        self.name = 'None'
        self.location = 'None'
        self.industries = 'None'
        self.stage = 'None'
        self.latest_funding = 'None'
        self.funded_date = 'None'
        self.desc = 'None'
        self.url = 'None'
        self.json = 'None'
        self.delimiter = '\t'
        self.empty_string = 'empty'

    def get_results(self):
        return self.name + self.delimiter + self.location + self.delimiter + self.industries + self.delimiter + self.stage + self.delimiter + self.latest_funding + self.delimiter + self.funded_date + self.delimiter + self.desc + self.delimiter + self.url + self.delimiter + self.json

    def clean_input(self, input):
        if input == None or input == '':
            return self.empty_string
        else:
            return input.replace('\n', ' ').replace('\r', ' ').encode('utf-8')

    def set_name(self, name):
        self.name = self.clean_input(name)

    def set_location(self, location):
        self.location = self.clean_input(location)

    def set_industries(self, industries):
        self.industries = self.clean_input(industries)

    def set_stage(self, stage):
        self.industries = self.clean_input(stage)

    def set_latest_funding(self, latest_funding):
        self.latest_funding = self.clean_input(latest_funding)

    def set_funded_date(self, funded_date):
        self.funded_date = self.clean_input(funded_date)

    def set_url(self, url):
        self.url = self.clean_input(url)

    def set_desc(self, desc):
        self.desc = self.clean_input(desc)

    def set_json(self, json):
        self.json = self.clean_input(json)


class LinkedInRecord:
    def __init__(self, input):
        self.name = input[0]
        self.image = input[1]
        self.position = input[2]
        self.linkedin = input[3]

    def dump(self):
        return {'name': self.name, 'image': self.image, 'position': self.position, 'linkedin': self.linkedin}
