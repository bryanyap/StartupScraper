class TechInAsiaRecord:
    def __init__(self, input):
        self.name = self.clean(input[0])
        self.location = self.clean(input[1])
        self.industries = self.clean(input[2])
        self.stage = self.clean(input[3])
        self.latest_funding = self.clean(input[4])
        self.funded_date = self.clean(input[5])
        self.desc = self.clean(input[6])
        delimiter = ','

        print self.name + delimiter + self.location + delimiter + self.industries + delimiter + self.stage + delimiter + self.latest_funding + delimiter + self.funded_date + delimiter + self.desc

    def clean(self, input):
        if input == None:
            return 'None'
        else:
            return input


class LinkedInRecord:
    def __init__(self, input):
        self.name = input[0]
        self.image = input[1]
        self.position = input[2]
        self.linkedin = input[3]

    def dump(self):
        return {'name': self.name, 'image': self.image, 'position': self.position, 'linkedin': self.linkedin}
