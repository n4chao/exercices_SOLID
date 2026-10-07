from models.reduction import Reduction

class ReductionVIP(Reduction):
    def calculer(self, prix: float) -> float:   
        if prix > 50.0:
            return prix * 0.70
        return prix