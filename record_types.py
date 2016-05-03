class TechInAsiaRecord:
    def __init__(self, input):
        self.name = self.cleanAndEncode(input[0])
        self.location = self.cleanAndEncode(input[1])
        self.industries = self.cleanAndEncode(input[2])
        self.stage = self.cleanAndEncode(input[3])
        self.latest_funding = self.cleanAndEncode(input[4])
        self.funded_date = self.cleanAndEncode(input[5])
        self.desc = self.cleanAndEncode(input[6])
        self.delimiter = '|'

        # print self.name + delimiter + self.location + delimiter + self.industries + delimiter + self.stage + delimiter + self.latest_funding + delimiter + self.funded_date + delimiter + self.desc

    def cleanAndEncode(self, input):
        if input == None:
            return 'None'
        else:
            return input.encode('utf-8')

    def getResults(self):
        delimiter = self.delimiter
        return self.name + delimiter + self.location + delimiter + self.industries + delimiter + self.stage + delimiter + self.latest_funding + delimiter + self.funded_date + delimiter + self.desc


class LinkedInRecord:
    def __init__(self, input):
        self.name = input[0]
        self.image = input[1]
        self.position = input[2]
        self.linkedin = input[3]

    def dump(self):
        return {'name': self.name, 'image': self.image, 'position': self.position, 'linkedin': self.linkedin}
