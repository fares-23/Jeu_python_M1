import pygame
from personnage import Personnage

class Archer(Personnage):
    def __init__(self, x, y,couleur_perso):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.couleur_perso = couleur_perso  # Redéfini pour l'archer
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 4  # Vitesse spécifique à l'archer
        self.esquive = 0.3

    def deplacement(self,grille,event,coordonnee):
        super().deplacement(grille,event,coordonnee)
    
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        super().afficher_deplacement(grille,fenetre,coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)
    