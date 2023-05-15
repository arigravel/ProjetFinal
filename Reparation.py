# Arianne Gravel
# 1928883

from datetime import datetime


class Reparation:
    """Définition de la classe"""

    # Définiton du constructeur - initialiser les attributs
    def __init__(self, code: int, description: str, montant: float, datereparation: datetime, codeemploye: int):
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

    # Les méthodes d'accès
    def get_code(self) -> int:
        return self.__code

    def set_code(self, value: int) -> None:
        self.__code = value

    def get_description(self) -> str:
        return self.__description

    def set_description(self, value: str) -> None:
        self.__description = value

    def get_montant(self) -> float:
        return self.__montant

    def set_montant(self, value: float) -> None:
        self.__montant = value

    def get_datereparation(self) -> datetime:
        return self.__datereparation

    def set_datereparation(self, value: datetime) -> None:
        self.__datereparation = value

    def get_codeemploye(self) -> int:
        return self.__codeemploye

    def set_codeemploye(self, value: int) -> None:
        self.__codeemploye = value
