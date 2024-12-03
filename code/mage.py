import pygame
from personnage import Personnage
from constante import *

class Mage(Personnage):
    def __init__(self, x, y,royaume = None):
        super().__init__(x, y) 
        self.image_path =  mage_path 
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 2 
        
        self.royaume = royaume

    def deplacement(self,grille,event,coordonnee):
        super().deplacement(grille,event,coordonnee)
    
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        super().afficher_deplacement(grille,fenetre,coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)