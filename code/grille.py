import pygame
import sys
from pytmx import load_pygame
from constante import *

# La classe Grille représente la grille du jeu, c'est-à-dire la collection de cases qui composent l'environnement de jeu.
class Grille:
    
    # Le constructeur __init__ initialise la grille en fonction de la taille en x et y, ainsi que les coordonnées de décalage.
    def __init__(self, taille_x, taille_y, x, y):
        # Taille en x et y de la grille, spécifiant combien de cases la grille aura en largeur et en hauteur.
        self.taille_x = taille_x
        self.taille_y = taille_y
        
        # Définition des offsets (décalages) en x et y pour la position de la grille sur l'écran.
        self.offset_x = x
        self.offset_y = y
        
        # Liste de listes (matrice) qui contient les cases de la grille.
        self.cases = []
        
        # Génération des cases de la grille, chaque case est un rectangle de Pygame avec les dimensions de la case.
        for i in range(taille_y):
            ligne = []  # Liste pour stocker la ligne de cases
            for j in range(taille_x):
                # Création d'un rectangle pour chaque case, basé sur les coordonnées et la taille de la case.
                ligne.append(pygame.Rect(j * TAILLE_CASE + x, i * TAILLE_CASE + y, TAILLE_CASE, TAILLE_CASE))
            # Ajout de la ligne à la grille.
            self.cases.append(ligne)
        
        # Calcul de la largeur et de la hauteur totale de la grille en pixels.
        self.largeur = taille_x * TAILLE_CASE
        self.hauteur = taille_y * TAILLE_CASE

    # La méthode afficher dessine la grille et les tuiles de la carte à l'écran.
    def afficher(self, fenetre, tmx_data):
        # Afficher les tuiles du fichier TMX
        # Parcourt chaque calque visible dans les données de la carte TMX (fichier de carte).
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "tiles"):  # Vérifie si le calque a des tuiles
                # Parcourt chaque tuile (x, y) dans le calque.
                for x, y, tile in layer.tiles():
                    if tile:  # Vérifie que la tuile existe
                        # Affiche la tuile sur la fenêtre en la déplaçant à la position (x, y) avec les offsets.
                        fenetre.blit(tile, (x * TAILLE_CASE + self.offset_x, y * TAILLE_CASE + self.offset_y))

        # Dessiner une grille transparente sur la fenêtre
        # Crée une surface transparente pour dessiner les lignes de la grille.
        surface = pygame.Surface(fenetre.get_size(), pygame.SRCALPHA)  # Surface avec canal alpha pour la transparence
        TRANSPARENT = (255, 255, 255, 0)  # Couleur blanche avec opacité 0 (complètement transparent)
        
        # Dessine chaque case de la grille.
        for ligne in self.cases:
            for case in ligne:
                pygame.draw.rect(surface, TRANSPARENT, case, 1)  # Dessine une ligne pour chaque case (épaisseur de 1 pixel)
        
        # Affiche la surface transparente avec les lignes de la grille sur la fenêtre.
        fenetre.blit(surface, (0, 0))  # Place la surface de la grille sur la fenêtre
