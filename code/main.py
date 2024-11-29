import pygame
import sys
from pytmx import load_pygame
from constante import *
from grille import Grille
from menu import Menu
from bouton import Bouton
from jeu import Jeu
from selection import Selection


class Main:
    pygame.init()

    def __init__(self):
        # Initialisation de la fenêtre Pygame
        self.fenetre = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Jeu avec Tiled")

        # Charger la carte TMX
        try:
            self.tmx_data = load_pygame("C:/Users/melaa/Desktop/Jeu_python_M1/map.tmx")
            print("Carte TMX chargée avec succès")
        except Exception as e:
            print(f"Erreur lors du chargement de la carte : {e}")
            pygame.quit()
            sys.exit()

        # Créer une instance de Grille pour gérer les cases
        self.grille = Grille(taille_x=120, taille_y=120, x=0, y=0)
        
        # Initialisation des autres composants du jeu (Menu, Sélection, Jeu)
        self.menu = Menu(self.fenetre)
        self.selection = Selection(self.fenetre)
        self.jeu = Jeu()
        
        # Initialisation de l'état du jeu (menu au départ)
        self.etat = "menu"

    def boucle_principale(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.etat == "menu":
                        self.etat = self.menu.verifier_clic(event)
                    elif self.etat == "selection":
                        self.etat = self.selection.gerer_evenements(event)
                    elif self.etat == "jeu":
                        self.jeu.verifier_clic(event)

            # Remplir l'écran avec une couleur de fond
            self.fenetre.fill((0, 0, 0))  # Fond noir pour vérifier l'affichage

            # Afficher la carte TMX à l'écran (utilisation de Grille pour la gestion des cases)
            self.grille.afficher(self.fenetre, self.tmx_data)

            # Afficher le contenu en fonction de l'état actuel du jeu
            if self.etat == "menu":
                self.menu.afficher()
            elif self.etat == "selection":
                self.selection.dessiner(self.fenetre)
            elif self.etat == "jeu":
                self.jeu.afficher(self.fenetre)

            # Mettre à jour l'affichage à chaque itération
            pygame.display.flip()
            pygame.display.update()

            # Limiter la boucle à 60 FPS
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    start = Main()
    start.boucle_principale()
