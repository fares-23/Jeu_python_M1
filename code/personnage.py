import pygame
from constante import *
import sys
from bandeau_inferieur import BandeauInferieur
from abc import ABC, abstractmethod
import random
from carte import Carte

class Personnage(ABC):
    
    def __init__(self, x, y,image_path):
        #variables de personnage
        self.nom = None
        self.attaque = None
        self.defense = None
        self.pv = None
        self.vitesse = None
        self.esquive = None
        self.royaume = None
        
        self.action = None # True si le personnage n'a pas encore joué, False sinon
        
        self.rect = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
        self.selectionne = False
        self.afficher_deplacement_possible = False
        
        self.image_path = None
        
        self.bandeau = BandeauInferieur()
        self.zone = []
        self.zone_attaque = []
        self.coordonnee = None
        self.boue = []
        self.arbre = []
        self.carte = []
        
    def afficher_deplacement(self, grille, fenetre, coordonnee, carte):
        self.carte = carte
        self.coordonnee = coordonnee
        self.arbre = [] + carte.recuperer_coordonnees_calque("arbre")
        self.boue = [] + carte.recuperer_coordonnees_calque("boue")
        if self.afficher_deplacement_possible:
            # Récupération des coordonnées des obstacles
            obstacles = (
                carte.recuperer_coordonnees_calque("maison")
                + carte.recuperer_coordonnees_calque("eau")
                + carte.recuperer_coordonnees_calque("rocher")
            )
            
            for ligne in grille:
                for case in ligne:
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE

                    # Ignore les cases hors de portée ou déjà occupées
                    if abs(dx) + abs(dy) > self.vitesse or (case.x, case.y) in coordonnee:
                        continue

                    # Vérifie s'il y a un obstacle bloquant la case
                    is_blocked = False
                    for obstacle in obstacles:
                        # Bloque la progression si un obstacle se trouve sur la trajectoire
                        if (
                            # Horizontalement à droite
                            dx > 0
                            and case.y == obstacle[1]
                            and obstacle[0] <= case.x <= obstacle[0] + (dx - 1) * TAILLE_CASE
                        ) or (
                            # Horizontalement à gauche
                            dx < 0
                            and case.y == obstacle[1]
                            and obstacle[0] >= case.x >= obstacle[0] + (dx + 1) * TAILLE_CASE
                        ) or (
                            # Verticalement en bas
                            dy > 0
                            and case.x == obstacle[0]
                            and obstacle[1] <= case.y <= obstacle[1] + (dy - 1) * TAILLE_CASE
                        ) or (
                            # Verticalement en haut
                            dy < 0
                            and case.x == obstacle[0]
                            and obstacle[1] >= case.y >= obstacle[1] + (dy + 1) * TAILLE_CASE
                        ):
                            is_blocked = True
                            break

                    if not is_blocked:
                        # Dessine la case valide
                        pygame.draw.rect(fenetre, (16, 16, 205), case, 1)
                        self.bandeau.afficher_personnage(
                            fenetre, self.image_path, self.pv, self.attaque, self.defense,self.esquive,self.royaume
                        )
                        self.zone.append((case.x, case.y))
            
    def deplacement(self, grille, event, coordonnee, carte):
        if self.action:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    # Activer ou désactiver la sélection du personnage
                    self.selectionne = not self.selectionne
                    self.afficher_deplacement_possible = self.selectionne
                else:
                    for ligne in grille.cases:
                        for case in ligne:
                            if case.collidepoint(mouse_pos) and self.selectionne:
                                dx = (case.x - self.rect.x) // TAILLE_CASE
                                dy = (case.y - self.rect.y) // TAILLE_CASE

                                # Ignore les cases hors de portée ou déjà occupées
                                if abs(dx) + abs(dy) > self.vitesse or (case.x, case.y) in coordonnee:
                                    continue

                                # Vérifie s'il y a un obstacle bloquant la case
                                obstacles = (
                                    carte.recuperer_coordonnees_calque("maison")
                                    + carte.recuperer_coordonnees_calque("eau")
                                    + carte.recuperer_coordonnees_calque("rocher")
                                )
                                is_blocked = False
                                for obstacle in obstacles:
                                    # Bloque la progression si un obstacle se trouve sur la trajectoire
                                    if (
                                        # Horizontalement à droite
                                        dx > 0
                                        and case.y == obstacle[1]
                                        and obstacle[0] <= case.x <= obstacle[0] + (dx - 1) * TAILLE_CASE
                                    ) or (
                                        # Horizontalement à gauche
                                        dx < 0
                                        and case.y == obstacle[1]
                                        and obstacle[0] >= case.x >= obstacle[0] + (dx + 1) * TAILLE_CASE
                                    ) or (
                                        # Verticalement en bas
                                        dy > 0
                                        and case.x == obstacle[0]
                                        and obstacle[1] <= case.y <= obstacle[1] + (dy - 1) * TAILLE_CASE
                                    ) or (
                                        # Verticalement en haut
                                        dy < 0
                                        and case.x == obstacle[0]
                                        and obstacle[1] >= case.y >= obstacle[1] + (dy + 1) * TAILLE_CASE
                                    ):
                                        is_blocked = True
                                        break

                                if not is_blocked:
                                    self.rect.x = case.x
                                    self.rect.y = case.y
                                    self.afficher_deplacement_possible = False
                                    self.selectionne = False
                                    self.action = False
                                    return

    def afficher_personnage(self, fenetre,liste_royaume=None):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (TAILLE_CASE, TAILLE_CASE))
        if self.royaume == liste_royaume[0]:
            image =  pygame.transform.flip(image,True,False) #retourne l'image verticalement
        fenetre.blit(image, self.rect)
    
    def get_coordonnees(self):
        return (self.rect.x, self.rect.y)

    def zone_combat(self, fenetre, grille):
        if self.nom == "archer" or self.nom == "mage":
            for ligne in grille:
                for case in ligne:
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE
                    if (case.x, case.y) in self.coordonnee:
                        pass
                    elif abs(dx) + abs(dy) <= self.vitesse:
                        pygame.draw.rect(fenetre, ROUGE, case, 1)
                        self.bandeau.afficher_personnage(fenetre, self.image_path, self.pv, self.attaque, self.defense,self.esquive,self.royaume)
                        self.zone_attaque.append((case.x, case.y))
        else:
            # Zone d'attaque au corps à corps
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x = self.rect.x // TAILLE_CASE + dx
                    y = self.rect.y // TAILLE_CASE + dy
                    if 0 <= x < len(grille[0]) and 0 <= y < len(grille):
                        case = grille[y][x]
                        pygame.draw.rect(fenetre, ROUGE, case, 1)
                        self.zone_attaque.append((case.x, case.y))

    @abstractmethod
    def competence(self,cible,fenetre):
        pass
      
    def recevoir_attaque(self, degats,fenetre):
         #Gère les dégâts reçus en tenant compte de l'esquive.
        if random.random() < self.esquive:
            self.bandeau.afficher_message(f"{self.nom} esquive l'attaque !",fenetre)
            pygame.display.flip()
            pygame.time.wait(500)
        else:
            self.pv -= max(degats, 0) # max(0, degats) pour éviter les PV négatifs
            self.bandeau.afficher_message(f"{self.nom} reçoit {degats} dégâts !",fenetre)
            pygame.display.flip()
            pygame.time.wait(500)
        
    def soigner(self, soin,fenetre):
        self.pv += soin
        self.bandeau.afficher_message(f"{self.nom} récupère {soin} PV !",fenetre)

    def buff(self, buff,fenetre):
        self.defense += buff
        self.bandeau.afficher_message(f"{self.nom} gagne {buff} points de défense !",fenetre)

    @abstractmethod
    def carte_effet(self):
        pass
                        
                        