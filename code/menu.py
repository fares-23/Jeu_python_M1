import pygame
from bouton import Bouton
from constante import *
import sys

# La classe Menu gère l'affichage et l'interaction avec le menu principal du jeu.
# Elle permet à l'utilisateur de démarrer une nouvelle partie ou de quitter le jeu.
class Menu:
    
    # Le constructeur initialise les éléments nécessaires pour le menu, tels que les boutons et les images.
    def __init__(self, fenetre):
        self.fenetre = fenetre  # La fenêtre dans laquelle le menu sera affiché
        
        # Chargement des images pour les boutons du menu (inactif et au survol)
        self.image = [pygame.image.load("assets/interface/MenuButtonInactiv.png"),
                      pygame.image.load("assets/interface/MenuButtonPreLight.png")]
        
        # Création des boutons "Start" et "Quit"
        self.boutons = [            
            Bouton("Start", self.fenetre.get_width() // 2 - 50, self.fenetre.get_height() // 2 - 80, 100, 50, NOIR, self.image[0], self.image[1]),
            Bouton("Quit", self.fenetre.get_width() // 2 - 50, self.fenetre.get_height() // 2 - 20, 100, 50, NOIR, self.image[0], self.image[1])
        ]

    # La méthode afficher gère l'affichage des boutons sur l'écran.
    def afficher(self):
        # Affiche tous les boutons présents dans la liste 'self.boutons'
        for bouton in self.boutons:
            bouton.afficher(self.fenetre)

    # La méthode verifier_clic gère l'événement de clic de souris sur les boutons du menu.
    def verifier_clic(self, event):
        # Parcourt tous les boutons pour vérifier si le clic de souris se produit sur l'un d'entre eux
        for bouton in self.boutons:
            # Vérifie si la position du clic est à l'intérieur des limites du bouton
            if bouton.x < event.pos[0] < bouton.x + bouton.width and bouton.y < event.pos[1] < bouton.y + bouton.height:
                if bouton.text == "Start":
                    # Si le bouton "Start" est cliqué, retourne "selection" pour passer à la phase de sélection des royaumes
                    return "selection"
                elif bouton.text == "Quit":
                    # Si le bouton "Quit" est cliqué, ferme le jeu
                    pygame.quit()
                    sys.exit()
        # Si aucun bouton n'a été cliqué, retourne "menu" pour revenir au menu principal
        return "menu"
