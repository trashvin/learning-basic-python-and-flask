class AgePrediction:

    def __init__(self):
        self.name = ''
        self.gender = ''
        self.probability = 0

    def parse(self, response_dict):
        self.name = response_dict['name']
        self.gender = response_dict['gender']
        self.probability = float(response_dict['probability']) * 100