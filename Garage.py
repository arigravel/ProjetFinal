# Arianne Gravel
# 1928883

from Employe import *
from Voiture import *


class Garage:
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, nom: str, adresse: str, telephone: str):
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.__employes: list[Employe] = []
        self.__voitures: list[Voiture] = []

    # Les méthodes d'accès
    def get_nom(self) -> str:
        return self.__nom

    def set_nom(self, value: str) -> None:
        self.__nom = value

    def get_adresse(self) -> str:
        return self.__adresse

    def set_adresse(self, value: str) -> None:
        self.__adresse = value

    def get_telephone(self) -> str:
        return self.__telephone

    def set_telephone(self, value: str) -> None:
        self.__telephone = value

    # Les autres méthodes

    # Sérialise en format JSON un objet de type "Garage" vers un fichier
    def serialisergarage(cls, element: Garage, fichier: str) -> None:
        pass

    # Désérialise un fichier en format JSON qu'elle reçoit en paramètre vers un objet de type "Garage"
    def deserialisergarage(cls, fichier: str) -> Garage:
        pass

    # Ajoute un objet de type "Voiture" qu'elle reçoit en paramètre à l'attribut "voitures" de la classe "Garage"
    def ajoutervoiture(self, element: Voiture) -> None:
        pass

    # Retourne un objet de type "Voiture" dont le numéro de plaque est donné en paramètre
    def getvoiture(self, numvoiture: str) -> Voiture:
        pass

    # Ajoute un objet de type "Reparation" qu'elle reçoit en paramètre à l'attribut "reparations" de la classe "Voiture"
    def ajouterreparation(self, numvoiture: str, reparation: Reparation) -> None:
        pass

    # Retourne un objet de type "list[Reparation]" de la voiture dont le numéro de plaque est donné en paramètre
    def getreparation(self, numvoiture: str) -> list[Reparation]:
        pass
