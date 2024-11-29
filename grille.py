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

def obtenir_case(self, position):
    """
    Renvoie la case correspondant à une position donnée.
    :param position: Tuple (x, y) représentant la position en pixels.
    :return: Tuple (ligne, colonne) de la case.
    """
    x, y = position
    col = x // TAILLE_CASE
    row = y // TAILLE_CASE

    if 0 <= row < self.taille and 0 <= col < self.taille:
        return row, col
    return None  # Si la position est hors de la grille

def est_case_valide(self, row, col):
    """
    Vérifie si une case est valide pour un déplacement.
    :param row: Ligne de la case.
    :param col: Colonne de la case.
    :return: True si la case est valide, False sinon.
    """
    return 0 <= row < self.taille and 0 <= col < self.taille

def afficher_deplacement_possible(self, personnage):
    """
    Affiche les cases accessibles pour un personnage en fonction de sa vitesse.
    :param personnage: Instance d'un personnage (Archer, Mage, Chevalier).
    """
    range_max = personnage.vitesse
    row, col = personnage.get_coordonnees()

    for i in range(-range_max, range_max + 1):
        for j in range(-range_max, range_max + 1):
            new_row, new_col = row + i, col + j
            if self.est_case_valide(new_row, new_col):
                case = self.cases[new_row][new_col]
                pygame.draw.rect(self.fenetre, COULEUR_DEPLACEMENT, case, 2)

def deplacer_personnage(self, personnage, event):
    """
    Gère le déplacement d'un personnage sur la grille après un clic valide.
    :param personnage: Instance d'un personnage (Archer, Mage, Chevalier).
    :param event: Événement Pygame contenant la position du clic.
    """
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
        pos = event.pos  # Position du clic en pixels
        case = self.obtenir_case(pos)  # Récupère la case cliquée
        if case:
            row, col = case
            personnage.set_coordonnees(row, col)  # Met à jour les coordonnées du personnage
