from abc import ABC, abstractmethod

class BasePlatform(ABC):
    @abstractmethod
    def extract_message(self, data: dict) -> str:
        ...

    @abstractmethod
    def extract_token(self, data: dict) -> str:
        ...
