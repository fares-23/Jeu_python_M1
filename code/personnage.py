import pygame
from constante import *
import sys


class Personnage:
    
    def __init__(self, x, y,):
        #variables de personnage
        self.couleur_perso = (255, 0, 0)
        self.attaque = 0
        self.defense = 0
        self.pv = 0
        self.vitesse = 3
        
        self.rect = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
        self.selectionne = False
        self.afficher_deplacement_possible = False
        
        self.image_path = None
        
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        if self.afficher_deplacement_possible:
            for ligne in grille:
                for case in ligne:
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE
                    if (case.x,case.y) in coordonnee:
                        pass
                    elif abs(dx) + abs(dy) <= self.vitesse:
                        pygame.draw.rect(fenetre, COULEUR_DEPLACEMENT, case)
                        pygame.draw.rect(fenetre, (0, 0, 255), case, 1)
                        
    def afficher_personnage(self, fenetre):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (TAILLE_CASE, TAILLE_CASE))
        fenetre.blit(image, self.rect)

    def deplacement(self, grille,event,coordonnee):
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
                self.selectionne = False 
                self.afficher_deplacement_possible = False 

    def combat(self):
        print("combat")
        
    def get_coordonnees(self):
        return (self.rect.x, self.rect.y)