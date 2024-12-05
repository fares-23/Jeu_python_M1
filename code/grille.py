import pygame
import sys
from pytmx import load_pygame
from constante import *

class Grille:
    def __init__(self, taille_x, taille_y, x, y):
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.offset_x = x
        self.offset_y = y
        self.cases = []
        for i in range(taille_y):
            ligne = []
            for j in range(taille_x):
                ligne.append(pygame.Rect(j * TAILLE_CASE + x, i * TAILLE_CASE + y, TAILLE_CASE, TAILLE_CASE))
            self.cases.append(ligne)
        self.largeur = taille_x * TAILLE_CASE
        self.hauteur = taille_y * TAILLE_CASE

    def afficher(self, fenetre, tmx_data):
        # Afficher les tuiles du fichier TMX
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "tiles"):
                for x, y, tile in layer.tiles():
                    if tile:  # Vérifie que la tuile existe
                        fenetre.blit(tile, (x * TAILLE_CASE + self.offset_x, y * TAILLE_CASE + self.offset_y))

        # Dessiner une grille transparente sur la fenêtre
        surface = pygame.Surface(fenetre.get_size(), pygame.SRCALPHA)  # Surface avec canal alpha
        TRANSPARENT = (255, 255, 255, 0)  # Couleur blanche avec opacité de 50
        for ligne in self.cases:
            for case in ligne:
                pygame.draw.rect(surface, TRANSPARENT, case, 1)  # Dessine la grille sur la surface
        fenetre.blit(surface, (0, 0))  # Affiche la surface transparente sur la fenêtre

 
