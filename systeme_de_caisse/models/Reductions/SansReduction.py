from models.reduction import Reduction

class SansReduction(Reduction):
    def calculer(self, prix: float) -> float:   
        return prix