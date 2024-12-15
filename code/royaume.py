import pygame
from abc import ABC, abstractmethod

# La classe Royaume est une classe abstraite qui définit le concept d'un royaume dans le jeu.
# Elle est héritée par des classes concrètes représentant des royaumes spécifiques (par exemple, Empire Adrastien, etc.)
class Royaume(ABC):
    
    # Le constructeur initialise la classe. Comme il s'agit d'une classe abstraite, 
    # le constructeur est vide, mais il est nécessaire pour que les sous-classes puissent l'étendre.
    def __init__(self):
        pass  # Aucun traitement spécifique n'est effectué ici.

    # La méthode armee est une méthode abstraite.
    # Chaque sous-classe devra fournir une implémentation spécifique de cette méthode pour définir la façon dont l'armée du royaume est générée.
    # Cette méthode n'a pas de corps dans cette classe car elle doit être définie dans les sous-classes.
    @abstractmethod
    def armee(self):
        pass  # Cette méthode doit être implémentée dans chaque sous-classe de Royaume pour créer l'armée du royaume.
