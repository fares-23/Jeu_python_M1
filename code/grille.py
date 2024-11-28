from constante import *
import pygame
import sys

class Grille:
    def __init__(self, taille_x, taille_y, x, y):
        self.cases = []
        for i in range(taille_y):
            ligne = []
            for j in range(taille_x):
                ligne.append(pygame.Rect(j * TAILLE_CASE + x, i * TAILLE_CASE + y, TAILLE_CASE, TAILLE_CASE))
            self.cases.append(ligne)

    def afficher(self, fenetre):
        for ligne in self.cases:
            for case in ligne:
                pygame.draw.rect(fenetre, COULEUR_GRILLE, case, 1)