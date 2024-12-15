import pygame
import sys
from pytmx import load_pygame
from constante import *

# La classe Jeu gère le déroulement de la partie, y compris l'affichage des personnages, la gestion des déplacements, et les actions des personnages.
class Jeu:
    
    # Le constructeur initialise les paramètres de la grille, des personnages et des autres éléments du jeu.
    def __init__(self):
        # Taille de la grille en fonction de la résolution de l'écran et de la taille des cases.
        taille_x = RESOLUTION[0] // TAILLE_CASE
        taille_y = RESOLUTION[1] // TAILLE_CASE

        # Création de la grille du jeu
        self.grille = Grille(taille_x, taille_y, 0, 0)

        # Liste des personnages du jeu
        self.__liste_personnage = []
        # Tour actuel du jeu
        self.__tour = 0
        # Indicateur pour passer au tour suivant
        self.__next_tour = False
        # Bandeau pour afficher les informations du jeu (par exemple, tour actuel)
        self.__bandeau = BandeauInferieur()
        # Liste des royaumes dans le jeu
        self.__liste_royaume = None
        # Carte du jeu
        self.carte = None
        
    # La méthode afficher permet d'afficher la grille, les personnages et les informations de bandeau sur la fenêtre de jeu.
    def afficher(self, fenetre, tmx_data, carte, liste_royaume=None):
        # Affiche la grille sur la fenêtre
        self.grille.afficher(fenetre, tmx_data)
        # Affiche les informations du bandeau (ex. : tour actuel)
        self.__bandeau.afficher(fenetre)
        self.__bandeau.afficher_tour(fenetre, self.tour)
        
        # Affiche chaque personnage dans la liste des personnages
        for i in range(len(self.__liste_personnage)):
            self.__liste_personnage[i].afficher_deplacement(self.grille.cases, fenetre, self.__liste_personnage[i].get_coordonnees(), carte)
            self.__liste_personnage[i].afficher_personnage(fenetre, liste_royaume)
            self.__liste_personnage[i].carte_effet()
        
    # La méthode verifier_clic gère les événements de clic de souris pour déplacer les personnages ou effectuer des actions.
    def verifier_clic(self, event, carte, liste_royaume=None):
        # Mise à jour des royaumes et de la carte
        self.__liste_royaume = liste_royaume
        self.carte = carte
        coordonnee = []
        
        # Collecte des coordonnées de tous les personnages
        for i in range(len(self.__liste_personnage)):
            coordonnee.append(self.__liste_personnage[i].get_coordonnees())
        
        # Gère les déplacements des personnages
        action = []
        for i in range(len(self.__liste_personnage)):
            # Si c'est le tour d'un personnage, on lui permet de se déplacer
            if self.__liste_personnage[i].royaume == self.__liste_royaume[self.tour % 2]:
                self.__liste_personnage[i].deplacement(self.grille, event, coordonnee, self.carte)
                action.append(self.__liste_personnage[i].action)
                
        # Si au moins un personnage a effectué une action, on ne passe pas au tour suivant
        if True in action:
            self.__next_tour = False
        else:
            # Sinon, le tour suivant commence
            self.__next_tour = True
            self.__tour += 1
            for i in range(len(self.__liste_personnage)):
                self.__liste_personnage[i].action = True
    
    # Propriétés pour accéder à la liste des personnages et au tour actuel
    @property
    def liste_personnage(self):
        return self.__liste_personnage
    
    @liste_personnage.setter
    def liste_personnage(self, new):
        self.__liste_personnage = new
    
    @property
    def tour(self):
        return self.__tour
    
    # La méthode combat gère la sélection de la cible par le joueur et effectue le combat.
    def combat(self, perso_selectionne, fenetre):
        # Affiche la zone de combat pour le personnage sélectionné
        perso_selectionne.zone_combat(fenetre, self.grille.cases)
        # Change la forme de la souris pour indiquer la sélection
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        
        cible = None
        self.__bandeau.afficher_message("Selectionner une cible (pour quitter selectionner une cible hors de porté).", fenetre)
        pygame.display.flip()
        
        # Attente du clic sur la cible
        while cible is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifie si un personnage est sélectionné comme cible
                    for perso in self.liste_personnage:
                        if perso.rect.collidepoint(event.pos) and perso != perso_selectionne and perso.royaume != perso_selectionne.royaume:
                            cible = perso
                            # Vérifie si la cible est dans la portée du personnage sélectionné
                            self.verifier_clic(event, self.carte, self.__liste_royaume)
                            if cible.get_coordonnees() not in perso_selectionne.zone_attaque:
                                self.__bandeau.afficher_message("La cible impossible", fenetre)
                                pygame.display.flip()
                                pygame.time.wait(500)
                                return
                            # Lance l'attaque de la compétence du personnage sélectionné
                            perso_selectionne.competence(cible, fenetre)
                            return

    # La méthode victoire vérifie si un des royaumes a gagné (si l'autre royaume n'a plus de troupes).
    def victoire(self):
        r1 = 0
        r2 = 0
        if self.__liste_personnage != None and self.__liste_royaume != None:
            for i in range(len(self.__liste_personnage)):
                if self.__liste_personnage[i].royaume == self.__liste_royaume[0]:
                    r1 += 1
                elif self.__liste_personnage[i].royaume == self.__liste_royaume[1]:
                    r2 += 1
            # Si un royaume n'a plus de troupes, il a perdu et l'autre a gagné
            if r1 == 0:
                return self.__liste_royaume[0]
            elif r2 == 0:
                return self.__liste_royaume[1]
    
    # La méthode mort gère la suppression des personnages morts (dont les points de vie sont égaux ou inférieurs à 0).
    def mort(self):
        if self.__liste_personnage != None:
            for i in range(len(self.__liste_personnage)):
                if self.__liste_personnage[i].pv <= 0:
                    self.__liste_personnage.pop(i)
                    break
            return self.__liste_personnage
