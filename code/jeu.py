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

        # self.arche = Archer(3 * TAILLE_CASE, 3 * TAILLE_CASE, (150, 0, 0))
        # self.mage = Mage(7 * TAILLE_CASE, 7 * TAILLE_CASE, (0, 150, 0))
        # self.chevalier = Chevalier(5 * TAILLE_CASE, 5 * TAILLE_CASE, (0, 0, 150))
        # self.liste_personnage = [self.arche, self.mage, self.chevalier]
        self.__liste_personnage = []
        
        
    def afficher(self, fenetre, tmx_data):
        self.grille.afficher(fenetre,tmx_data)
        for i in range(len(self.__liste_personnage)):
            self.__liste_personnage[i].afficher_deplacement(self.grille.cases,fenetre,self.__liste_personnage[i].get_coordonnees())
            self.__liste_personnage[i].afficher_personnage(fenetre)
        
    def verifier_clic(self, event):
        for i in range(len(self.__liste_personnage)):
            self.__liste_personnage[i].deplacement(self.grille,event,self.__liste_personnage[i].get_coordonnees())

            
    @property
    def liste_personnage(self):
        return self.__liste_personnage
    
    @liste_personnage.setter
    def liste_personnage(self, new):
        self.__liste_personnage = new
    
