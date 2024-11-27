from constante import *
import pygame
import sys

class Grille:
    def __init__(self, taille,fenetre):
        self.cases = []
        self.fenetre = fenetre
        for i in range(taille):
            ligne = []
            for j in range(taille):
                ligne.append(pygame.Rect(j * TAILLE_CASE, i * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            self.cases.append(ligne)

    def afficher(self):
        for ligne in self.cases:
            for case in ligne:
                pygame.draw.rect(self.fenetre, COULEUR_GRILLE, case, 1)

