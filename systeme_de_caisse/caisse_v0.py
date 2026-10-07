# caisse_v0.py  — VERSION INITIALE (code à refactoriser)
 
class Caisse:
 
    def calculer_total(self, prix: float, type_client: str) -> float:
        if type_client == "standard":
            return prix
        elif type_client == "etudiant":
            return prix * 0.85
        elif type_client == "fidele":
            if prix > 100.0:
                return prix * 0.80
            return prix
        elif type_client == "vip":
            if prix > 50.0:
                return prix * 0.70
            return prix
        else:
            return prix
 
 
# --- Test rapide ---
if __name__ == "__main__":
    caisse = Caisse()
    print(caisse.calculer_total(120.0, "etudiant"))   # attendu : 102.0
    print(caisse.calculer_total(120.0, "fidele"))     # attendu : 96.0
    print(caisse.calculer_total(40.0,  "fidele"))     # attendu : 40.0
    print(caisse.calculer_total(80.0,  "vip"))        # attendu : 56.0
    print(caisse.calculer_total(40.0,  "vip"))        # attendu : 40.0