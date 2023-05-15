# Arianne Gravel
# 1928883

from Employe import *
from Voiture import *
from Reparation import *
from pathlib import Path
import jsonpickle


class Garage(object):
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, nom: str, adresse: str, telephone: str, employes: list[Employe]):
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.set_employe(employes)
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

    def get_employe(self) -> list[Employe]:
        return self.__employe

    def set_employe(self, value: list[Employe]) -> None:
        self.__employe = value

    # Les autres méthodes

    def ajouter(self, value: Employe) -> None:
        self.__employe.append(value)

    # Sérialise en format JSON un objet de type "Garage" vers un fichier
    @classmethod
    def serialisergarage(cls, element: object, fichier: str) -> None:
        # ouvrir le fichier (creer le stream)
        path: Path = Path(fichier)
        stream = path.open('w')
        # serialiser l'élément vers le fichier
        strjson: str = jsonpickle.encode(element, indent=4, separators=(',', ':'))
        # Écrire le stream vers le ficher
        stream.write(strjson)

        # fermer le stream
        stream.flush()
        stream.close()

    # Désérialise un fichier en format JSON qu'elle reçoit en paramètre vers un objet de type "Garage"
    @classmethod
    def deserialisergarage(cls, fichier: str) -> object:
        # ouvrir le fichier (creer le stream)
        path: Path = Path(fichier)
        stream = path.open('r')
        # deserialiser le fichier vers un objet garage
        strjson = stream.read()  # Lire la chaine à partir du fichier
        reponse: object = jsonpickle.decode(strjson)

        # fermer le stream
        stream.close()
        # retourner le resultat
        return reponse

    # Ajoute un objet de type "Voiture" qu'elle reçoit en paramètre à l'attribut "voitures" de la classe "Garage"
    def ajoutervoiture(self, element: Voiture) -> None:
        self.__voitures.append(element)

    # Retourne un objet de type "Voiture" dont le numéro de plaque est donné en paramètre
    def getvoiture(self, numvoiture: str) -> Voiture:
        for element in self.__voitures:
            if element.get_numeroplaque() == numvoiture:
                return element

    # Ajoute un objet de type "Reparation" qu'elle reçoit en paramètre à l'attribut "reparations" de la classe "Voiture"
    def ajouterreparation(self, numvoiture: str, reparation: Reparation) -> None:
        self.ajouterreparation(numvoiture, reparation)

    # Retourne un objet de type "list[Reparation]" de la voiture dont le numéro de plaque est donné en paramètre
    def getreparation(self, numvoiture: str) -> list[Reparation]:
        reparation: Reparation
        for voiture in self.__voitures:
            if element.get_numeroplaque() == numvoiture:
                return self.ajouterreparation(voiture,reparation)
