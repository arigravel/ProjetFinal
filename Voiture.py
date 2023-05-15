# Arianne Gravel
# 1928883

from Client import *
from Reparation import *


class Voiture:
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, numeroplaque: str, marque: str, modele: str, couleur: str, annee: int, proprietaire: Client):
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_annee(annee)
        self.set_proprietaire(proprietaire)
        self.__reparations: list[Reparation] = []

    # Les méthodes d'accès
    def get_numeroplaque(self) -> str:
        return self.__numeroplaque

    def set_numeroplaque(self, value: str) -> None:
        self.__numeroplaque = value

    def get_marque(self) -> str:
        return self.__marque

    def set_marque(self, value: str) -> None:
        self.__marque = value

    def get_modele(self) -> str:
        return self.__modele

    def set_modele(self, value: str) -> None:
        self.__modele = value

    def get_couleur(self) -> str:
        return self.__couleur

    def set_couleur(self, value: str) -> None:
        self.__couleur = value

    def get_annee(self) -> int:
        return self.__annee

    def set_annee(self, value: int) -> None:
        self.__annee = value

    def get_proprietaire(self) -> Client:
        return self.__proprietaire

    def set_proprietaire(self, value: Client) -> None:
        self.__proprietaire = value

    # Les autres méthodes

    # Ajoute une réparation qu'elle reçoit en paramètre à la liste "reparations"
    def ajouterreparation(self, element: Reparation) -> None:
        self.__reparations.append(element)
