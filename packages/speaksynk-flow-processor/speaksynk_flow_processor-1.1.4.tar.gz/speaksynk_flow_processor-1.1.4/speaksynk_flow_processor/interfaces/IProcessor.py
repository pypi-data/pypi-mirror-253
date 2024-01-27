from abc import abstractmethod


class IProcessor:
    @abstractmethod
    def run(self):
        pass
