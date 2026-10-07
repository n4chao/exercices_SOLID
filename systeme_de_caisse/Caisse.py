from models.reduction import Reduction
from models.Reductions.ReductionEtudiant import ReductionEtudiant
from models.Reductions.ReductionFidele import ReductionFidele
from models.Reductions.ReductionVIP import ReductionVIP
from models.Reductions.SansReduction import SansReduction
from systeme_de_caisse.models import Prix

variables = [
    Prix(prix = 120.0, reduction = ReductionEtudiant()),
    Prix(prix = 120.0, reduction = ReductionFidele()),
    Prix(prix = 40.0, reduction = ReductionFidele()),
    Prix(prix = 80.0, reduction = ReductionVIP()),
    Prix(prix = 40.0, reduction = ReductionVIP())
]

