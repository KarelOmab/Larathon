from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def index(self):
        pass

    @abstractmethod
    def show(self, id):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def edit(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass
