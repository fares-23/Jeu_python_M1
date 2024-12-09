from constante import *
import pygame
from grille import Grille
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from bandeau_inferieur import BandeauInferieur
import sys

class Jeu:
    def __init__(self):

        taille_x = RESOLUTION[0] // TAILLE_CASE
        taille_y = RESOLUTION[1] // TAILLE_CASE

        # Création de la grille, du personnage
        self.grille = Grille(taille_x, taille_y, 0, 0)

        self.__liste_personnage = []
        self.__tour = 0
        self.__next_tour = False
        self.__bandeau = BandeauInferieur()
        self.__liste_royaume = None
        self.carte = None

        
    def afficher(self, fenetre, tmx_data,carte,liste_royaume=None):
        self.grille.afficher(fenetre,tmx_data)
        self.__bandeau.afficher(fenetre)
        self.__bandeau.afficher_tour(fenetre,self.tour)
        for i in range(len(self.__liste_personnage)):
            self.__liste_personnage[i].afficher_deplacement(self.grille.cases,fenetre,self.__liste_personnage[i].get_coordonnees(),carte)
            self.__liste_personnage[i].afficher_personnage(fenetre,liste_royaume)
            self.__liste_personnage[i].carte_effet()
            
        
    def verifier_clic(self, event,carte,liste_royaume=None):
        self.__liste_royaume = liste_royaume
        self.carte = carte
        coordonnee = []
        for i in range(len(self.__liste_personnage)):
            coordonnee.append(self.__liste_personnage[i].get_coordonnees())
            
        #gère les déplacements des personnages
        action = []
        for i in range(len(self.__liste_personnage)):
            
            if self.__liste_personnage[i].royaume == self.__liste_royaume[self.tour%2]:
                self.__liste_personnage[i].deplacement(self.grille,event,coordonnee,self.carte)
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
    
    def combat(self, perso_selectionne, fenetre):
        perso_selectionne.zone_combat(fenetre,self.grille.cases)
        # Changer la forme de la souris pour indiquer la sélection
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        # Variable pour stocker la cible sélectionnée
        cible = None
        self.__bandeau.afficher_message("Selectionner une cible (pour quitter selectionner une cible hors de porté).", fenetre)
        pygame.display.flip()
        # Boucle pour attendre la sélection de la cible
        while cible is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifier si la cible est un personnage
                    for perso in self.liste_personnage:
                        if perso.rect.collidepoint(event.pos) and perso != perso_selectionne and perso.royaume != perso_selectionne.royaume:
                            cible = perso
                            self.verifier_clic(event,self.carte,self.__liste_royaume)
                            if cible.get_coordonnees() not in perso_selectionne.zone_attaque:
                                self.__bandeau.afficher_message("La cible impossible", fenetre)
                                pygame.display.flip()
                                pygame.time.wait(500)
                                return
                            perso_selectionne.competence(cible, fenetre)
                            return

