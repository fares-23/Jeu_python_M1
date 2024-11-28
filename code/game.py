import pygame
from personnage import Personnage
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from grille import Grille
from constante import *
import sys


# Initialisation de Pygame
pygame.init()

fenetre = pygame.display.set_mode((900, 600))

# Calcul de la taille de la grille
taille_x = 1280 // TAILLE_CASE
taille_y = 720 // TAILLE_CASE

# Création de la grille, du personnage
grille = Grille(taille_x, taille_y, 0, 0)  # La grille est positionnée à 0, 0

arche = Archer(3 * TAILLE_CASE, 3 * TAILLE_CASE,(150, 0, 0)) # L'archer est positionné en (3, 3) de couleur rouge
mage = Mage(7 * TAILLE_CASE, 7 * TAILLE_CASE,(0, 150, 0)) # Le mage est positionné en (3, 3) de couleur verte
chevalier = Chevalier(5 * TAILLE_CASE, 5 * TAILLE_CASE,(0, 0, 150)) # Le chevalier est positionné en (3, 3) de couleur bleu

# Boucle principale
liste_personnage = [arche,mage,chevalier]

while True:   
    coordonnee = [arche.get_coordonnees(),mage.get_coordonnees(),chevalier.get_coordonnees()]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for personnage in liste_personnage:
                personnage.deplacement(grille,event,coordonnee)
            

    # Affichage de la grille
    fenetre.fill((255, 255, 255))
    grille.afficher(fenetre)
    
    for personnage in liste_personnage:
        personnage.afficher_deplacement(grille.cases,fenetre,coordonnee)
        personnage.afficher_personnage(fenetre)


    # Mise à jour de l'écran
    pygame.display.update()

