import pygame
from constante import *
import sys
from bandeau_inferieur import BandeauInferieur
from abc import ABC, abstractmethod
import random
class Personnage(ABC):
    
    def __init__(self, x, y):
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
        
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        if self.afficher_deplacement_possible:
            for ligne in grille:
                for case in ligne:
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE
                    if (case.x,case.y) in coordonnee:
                        pass
                    elif abs(dx) + abs(dy) <= self.vitesse:
                        pygame.draw.rect(fenetre, (16,16,205), case, 1)
                        self.bandeau.afficher_personnage(fenetre,self.image_path,self.pv,self.attaque,self.defense)
                        self.zone.append((case.x,case.y))

    def afficher_personnage(self, fenetre):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (TAILLE_CASE, TAILLE_CASE))
        fenetre.blit(image, self.rect)

    def deplacement(self, grille,event,coordonnee):
        if self.action == True:
            caseselectionnee = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    if self.selectionne: 
                        self.afficher_deplacement_possible = False
                        self.selectionne = False
                    else:
                        self.selectionne = True
                        self.afficher_deplacement_possible = True
                else:
                    for ligne in grille.cases:
                        for case in ligne:
                            if case.collidepoint(mouse_pos) and self.selectionne:
                                dx = (case.x - self.rect.x) // TAILLE_CASE
                                dy = (case.y - self.rect.y) // TAILLE_CASE

                                if (case.x,case.y) in coordonnee:
                                    self.afficher_deplacement_possible = False
                                    self.selectionne = False
                                    pass
                                
                                elif abs(dx) + abs(dy) <= self.vitesse:
                                    self.rect.x = case.x
                                    self.rect.y = case.y
                                    self.afficher_deplacement_possible = False
                                    self.selectionne = False
                                    self.action = False
                                    
                    self.selectionne = False 
                    self.afficher_deplacement_possible = False 
    
    def get_coordonnees(self):
        return (self.rect.x, self.rect.y)
    
    
    @abstractmethod
    def competence(self,cible,fenetre):
        pass
    
    
    def recevoir_attaque(self, degats,fenetre):
         #Gère les dégâts reçus en tenant compte de l'esquive.
        if random.random() < self.esquive:
            self.bandeau.afficher_message(f"{self.nom} esquive l'attaque !",fenetre)
            pygame.display.flip()
            pygame.time.wait(250)
        else:
            self.pv -= max(degats, 0) # max(0, degats) pour éviter les PV négatifs
            self.bandeau.afficher_message(f"{self.nom} reçoit {degats} dégâts !",fenetre)
            pygame.display.flip()
            pygame.time.wait(250)
        

    def soigner(self, soin,fenetre):
        self.pv += soin
        self.bandeau.afficher_message(f"{self.nom} récupère {soin} PV !",fenetre)

    def buff(self, buff,fenetre):
        self.defense += buff
        self.bandeau.afficher_message(f"{self.nom} gagne {buff} points de défense !",fenetre)