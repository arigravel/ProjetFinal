# Arianne Gravel
# 1928883
from Personne import *


class Employe(Personne):
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, code: int, nom: str, prenom: str, fonction: str):
        self.set_code(code)
        super().__init__(nom, prenom)
        self.set_fonction(fonction)

    # Les méthodes d'accès
    def get_code(self) -> int:
        return self.__code

    def set_code(self, value: int) -> None:
        self.__code = value

    def get_fonction(self) -> str:
        return self.__fonction

    def set_fonction(self, value: str) -> None:
        self.__fonction = value

    # Définition de la méthode d'affichage str
    def __str__(self) -> str:
        return f"Code : {self.get_code()}\n{super().__str__()}\nFonction : {self.get_fonction()}"
