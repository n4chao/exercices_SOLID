from models.reduction import Reduction

class Caisse:
    def __init__(self, prix : float, reduction: Reduction):
        self.prix = prix
        self.reduction = reduction

    def calculer(self) -> float:
        return self.reduction.calculer(self.prix)

    def set_reduction(self, reduction: Reduction):
        self.reduction = reduction  

    def get_reduction(self) -> Reduction:
        return self.reduction