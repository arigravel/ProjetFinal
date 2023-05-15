# Arianne Gravel
# 1928883

class Personne:
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, nom: str = "Nom test", prenom: str = "Prénom test"):
        self.set_nom(nom)
        self.set_prenom(prenom)

    # Les méthodes d'accès
    def get_nom(self) -> str:
        return self.__nom

    # Doit commencer par une lettre majuscule et avoir une longueur de 6 à 20 lettres alphabétiques
    def set_nom(self, value: str) -> None:
        if 6 <= value.__len__() <= 20 and value[0].isupper() and value[0].isalpha():
            self.__nom = value
        else:
            raise ValueError(
                '\nAttention! La longueur doit être comprise entre 6 et 20 caractères et doit commencer par une lettre majuscule')

    def get_prenom(self) -> str:
        return self.__prenom

    # # Doit commencer par une lettre majuscule et avoir une longueur de 6 à 20 lettres alphabétiques
    def set_prenom(self, value: str) -> None:
        if 6 <= value.__len__() <= 20 and value[0].isupper() and value[0].isalpha():
            self.__prenom = value
        else:
            raise ValueError(
                '\nAttention! La longueur doit être comprise entre 6 et 20 caractères et doit commencer par une lettre majuscule')

    # Définition de la méthode d'affichage str
    def __str__(self) -> str:
        return f"Nom : {self.get_nom()}\nPrénom : {self.get_prenom()}"
