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

        self.__liste_personnage = []
        self.__tour = 0
        self.__next_tour = False
        
    def afficher(self, fenetre, tmx_data):
        self.grille.afficher(fenetre,tmx_data)
        for i in range(len(self.__liste_personnage)):
            self.__liste_personnage[i].afficher_deplacement(self.grille.cases,fenetre,self.__liste_personnage[i].get_coordonnees())
            self.__liste_personnage[i].afficher_personnage(fenetre)
        
    def verifier_clic(self, event,liste_royaume):
        coordonnee = []
        for i in range(len(self.__liste_personnage)):
            coordonnee.append(self.__liste_personnage[i].get_coordonnees())
        
        #gère les déplacements des personnages
        action = []
        for i in range(len(self.__liste_personnage)):
            if self.__liste_personnage[i].royaume == liste_royaume[self.tour%2]:
                self.__liste_personnage[i].deplacement(self.grille,event,coordonnee)
                action.append(self.__liste_personnage[i].action)
                
        #gère les actions des personnages
        if True in action:
            self.__next_tour = False
        else:
            self.__next_tour = True
            self.__tour += 1
            for i in range(len(self.__liste_personnage)):
                self.__liste_personnage[i].action = True
        
    @property
    def liste_personnage(self):
        return self.__liste_personnage
    
    @liste_personnage.setter
    def liste_personnage(self, new):
        self.__liste_personnage = new
    
    @property
    def tour(self):
        return self.__tour
    
