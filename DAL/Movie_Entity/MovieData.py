
class MovieData:
    def __init__(self, id, name, earnings):
        self.id = id
        self.name = name
        self.earnings = earnings

    def __str__(self):
        return "id:{} ,name: {}, Opening week earnings: {}\n".format(self.id, self.name, self.earnings)
