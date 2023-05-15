# Arianne Gravel
# 1928883
from Personne import *


class Client(Personne):
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, nom: str, prenom: str, telephone: str, courriel: str):
        super().__init__(nom, prenom)
        self.set_telephone(telephone)
        self.set_courriel(courriel)

    # Les méthodes d'accès
    def get_telephone(self) -> str:
        return self.__telephone

    def set_telephone(self, value: str) -> None:
        self.__telephone = value

    def get_courriel(self) -> str:
        return self.__courriel

    def set_courriel(self, value: str) -> None:
        self.__courriel = value

    # Définition de la méthode d'affichage str
    def __str__(self) -> str:
        return f"{super().__str__()}\nTéléphone : {self.get_telephone()}\nCourriel : {self.get_courriel()}"
