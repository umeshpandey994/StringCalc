from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, numbers):
        raise NotImplemented
