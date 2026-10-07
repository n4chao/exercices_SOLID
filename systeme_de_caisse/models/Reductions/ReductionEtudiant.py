from models.reduction import Reduction

class ReductionEtudiant(Reduction):
    def calculer(self, prix: float) -> float:   
        return prix * 0.85