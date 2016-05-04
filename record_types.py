class TechInAsiaRecord:
    def __init__(self, input):
        self.name = self.cleanAndEncode(input[0])
        self.location = self.cleanAndEncode(input[1])
        self.industries = self.cleanAndEncode(input[2])
        self.stage = self.cleanAndEncode(input[3])
        self.latest_funding = self.cleanAndEncode(input[4])
        self.funded_date = self.cleanAndEncode(input[5])
        self.desc = self.cleanAndEncode(input[6])
        self.url = self.cleanAndEncode(input[7])
        self.delimiter = '\t'

    def cleanAndEncode(self, input):
        if input == None:
            return 'None'
        else:
            input = input.replace('\n', ' ').replace('\r', '')
            return input.encode('utf-8')

    def getResults(self):
        return self.name + self.delimiter + self.location + self.delimiter + self.industries + self.delimiter + self.stage + self.delimiter + self.latest_funding + self.delimiter + self.funded_date + self.delimiter + self.desc + self.delimiter + self.url


class LinkedInRecord:
    def __init__(self, input):
        self.name = input[0]
        self.image = input[1]
        self.position = input[2]
        self.linkedin = input[3]

    def dump(self):
        return {'name': self.name, 'image': self.image, 'position': self.position, 'linkedin': self.linkedin}
