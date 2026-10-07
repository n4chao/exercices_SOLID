from models.reduction import Reduction

class ReductionFidele(Reduction):
    def calculer(self, prix: float) -> float:   
        if prix > 100.0:
            return prix * 0.80
        return prix