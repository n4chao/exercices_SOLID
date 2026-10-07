from abc import ABC, abstractmethod

class Reduction(ABC):
    @abstractmethod
    def calculer(self, prix : float) -> float:
        pass