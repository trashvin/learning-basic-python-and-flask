class BMIData:
    def __init__(self, bmi, rating_description):
        self.bmi = bmi
        self.rating_description = rating_description

    def __str__(self):
        return f'data data -> value : {self.bmi} ; rating : {self.rating_description}'
