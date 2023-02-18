from abc import ABC, abstractmethod
from DAL.DatabaseHelper import DatabaseHelper


class BaseDal(ABC):

    def __init__(self):
        self.db = DatabaseHelper.getInstance()

    @abstractmethod
    def save(self, entity):
        pass
