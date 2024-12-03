import pygame
from personnage import Personnage
from constante import *

class Archer(Personnage):
    def __init__(self, x, y,royaume = None):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.image_path =  archer_path 
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 4  # Vitesse spécifique à l'archer
        self.esquive = 0.3
        
        self.royaume = royaume
        self.action = True
        
    def deplacement(self,grille,event,coordonnee):
        super().deplacement(grille,event,coordonnee)
    
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        super().afficher_deplacement(grille,fenetre,coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)
    