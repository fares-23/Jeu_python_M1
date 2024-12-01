from constante import *
import pygame
from grille import Grille
from archer import Archer
from mage import Mage
from chevalier import Chevalier


class Jeu:
    def __init__(self):
        
        taille_x = RESOLUTION[0] // TAILLE_CASE
        taille_y = RESOLUTION[1] // TAILLE_CASE

# Création de la grille, du personnage
        self.grille = Grille(taille_x, taille_y, 0, 0)
        #self.grille = Grille(TAILLE_GRILLE, pygame.display.set_mode((TAILLE_GRILLE * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE)))
        self.arche = Archer(3 * TAILLE_CASE, 3 * TAILLE_CASE, (150, 0, 0))
        self.mage = Mage(7 * TAILLE_CASE, 7 * TAILLE_CASE, (0, 150, 0))
        self.chevalier = Chevalier(5 * TAILLE_CASE, 5 * TAILLE_CASE, (0, 0, 150))
        
        self.liste_personnage = [self.arche, self.mage, self.chevalier]

    def afficher(self, fenetre, tmx_data):
        self.grille.afficher(fenetre,tmx_data)
        for personnage in self.liste_personnage:
            personnage.afficher_deplacement(self.grille.cases, fenetre, [self.arche.get_coordonnees(), self.mage.get_coordonnees(), self.chevalier.get_coordonnees()])
            personnage.afficher_personnage(fenetre)

    def verifier_clic(self, event):
        for personnage in self.liste_personnage:
            personnage.deplacement(self.grille, event, [self.arche.get_coordonnees(), self.mage.get_coordonnees(), self.chevalier.get_coordonnees()])
