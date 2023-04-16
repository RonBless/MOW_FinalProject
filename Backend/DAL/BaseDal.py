from abc import ABC, abstractmethod
from Backend.DAL.DatabaseHelper import DatabaseHelper


class BaseDal(ABC):

    def __init__(self):
        self.db = DatabaseHelper.getInstance()

    @abstractmethod
    def save(self, entity):
        pass
