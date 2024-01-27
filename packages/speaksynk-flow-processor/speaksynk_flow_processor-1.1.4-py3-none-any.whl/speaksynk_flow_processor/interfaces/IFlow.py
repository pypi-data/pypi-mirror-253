from abc import abstractmethod


class IFlow:
    @abstractmethod
    def download(self, filekey):
        pass

    @abstractmethod
    def upload(self, filekey, fileName):
        pass
