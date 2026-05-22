from typing import List
from abc import ABC, abstractmethod


class DriverHandlerInterface(ABC):
    @abstractmethod
    def average(self, numbers: List[float]) -> float:
        pass
