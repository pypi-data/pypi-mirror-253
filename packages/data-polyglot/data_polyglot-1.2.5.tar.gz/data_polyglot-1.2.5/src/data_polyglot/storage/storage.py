from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def create(self, path, value):
        pass

    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def update(self, path, value):
        pass

    @abstractmethod
    def delete(self, path):
        pass

    @abstractmethod
    def is_key_present(self, path):
        pass
