class SampleList:
    def __init__(self):
        self.id = 0
        self.name = ''

    def __str__(self):
        return f'data : id = {self.id} ; name = {self.name}'