from abc import ABC, abstractmethod


class BaseData(ABC):

    @abstractmethod
    def __dic__(self):
        pass
