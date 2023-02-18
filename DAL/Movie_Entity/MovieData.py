from DAL.BaseData import BaseData


class MovieData(BaseData):

    def __init__(self, name, earnings, release_date):
        self.name = name
        self.earnings = earnings
        self.release_date = release_date

    def __str__(self):
        return "name: {},release date: {}, Opening week earnings: {}\n".format(self.name, self.release_date,
                                                                               self.earnings)

    def __dic__(self):
        return {'name': self.name,
                'earnings': self.earnings,
                'release date': self.release_date,
                }
