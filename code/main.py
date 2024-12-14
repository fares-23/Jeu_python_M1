import pygame
import sys
from pytmx import load_pygame
from constante import *
from grille import Grille
from menu import Menu
from bouton import Bouton
from jeu import Jeu
from selection import Selection
from carte import Carte
import random

class Main:
    pygame.init()
    pygame.mixer.init()  # Initialisation du module audio

    def __init__(self):
        # Initialisation de la fenêtre Pygame
        self.fenetre = pygame.display.set_mode(RESOLUTION_JEU)
        pygame.display.set_caption("Fire Emblem les 3 Royaumes !")
        """
        # Charger l'icône
        icon = pygame.image.load("assets/logo.jpeg")
        # Définir l'icône
        pygame.display.set_icon(icon)
        """

        # Initialisation de la carte
        map = random.randint(1, 3)
        if map == 1:
            self.choix_map = "map1.tmx"
            self.coord_start = co_map1
        elif map == 2:
            self.choix_map = "map2.tmx"
            self.coord_start = co_map2
        else:
            self.choix_map = "map3.tmx"
            self.coord_start = co_map3
        
        try:
            self.carte = Carte(self.choix_map, offset_x=0, offset_y=0)
        except Exception as e:
            print(f"Erreur lors du chargement de la carte : {e}")
            pygame.quit()
            sys.exit() 
            
        self.carte.extraire_coordonnees_par_calque()
        
        # Créer une instance de Grille pour gérer les cases
        self.grille = Grille(taille_x=120, taille_y=120, x=0, y=0)
        
        # Initialisation des autres composants
        self.menu = Menu(self.fenetre)
        self.selection = Selection(self.fenetre)
        self.jeu = Jeu()
        self.fond = pygame.image.load("assets/interface/main_menu_background.jpg")
        self.fond = pygame.transform.scale(self.fond, RESOLUTION_JEU)

        # Chargement des musiques
        self.musique_menu = "assets/music/FE Three Houses OST - 1. Three Houses Main Theme (English).mp3"  # Musique pour le menu
        self.musique_jeu = "assets/music/FE Three Houses OST - 6. Fodlan Winds (Rain).mp3"  # Musique pour l'état "jeu"

        # Jouer la musique du menu
        self.jouer_musique(self.musique_menu, volume=0.1)
        
        # État initial
        self.etat = "menu"
        self.cpt_musique = 0
        
    def jouer_musique(self, fichier, volume=0.1):
        """Charge et joue une musique avec le volume spécifié."""
        pygame.mixer.music.stop()  # Arrêtez la musique actuelle
        pygame.mixer.music.load(fichier)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)  # Joue en boucle infinie

    def boucle_principale(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE and self.jeu.liste_personnage:
                        # Vérifiez si un personnage est sélectionné
                        for perso in self.jeu.liste_personnage:
                            if perso.action and perso.selectionne:
                                self.jeu.combat(perso, self.fenetre)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.etat == "menu":
                        self.etat = self.menu.verifier_clic(event)
                    elif self.etat == "selection":
                        self.etat = self.selection.gerer_evenements(event, self.coord_start)
                    elif self.etat == "jeu":

                        self.jeu.verifier_clic(event, self.carte, self.selection.liste_royaume)
                        
            self.jeu.liste_personnage = self.selection.liste_troupe

            # Remplir l'écran avec une couleur de fond
            self.fenetre.blit(self.fond, (0, 0))  # Dessinez l'image de fond

            # Afficher le contenu en fonction de l'état actuel du jeu
            if self.etat == "menu":
                self.menu.afficher()
            elif self.etat == "selection":
                self.selection.dessiner(self.fenetre)
            elif self.etat == "jeu":
                #musique de jeu
                if self.cpt_musique == 0:
                    self.jouer_musique(self.musique_jeu, volume=0.1)
                    self.cpt_musique += 1
                    
                self.carte.afficher(self.fenetre)  # Affiche la carte
                self.jeu.afficher(self.fenetre, self.carte.tmx_data, self.carte, self.selection.liste_royaume)
                self.jeu.mort()
                if self.selection.liste_royaume != None:
                    if self.jeu.victoire() == self.selection.liste_royaume[0]:
                        result = self.afficher_victoire(self.selection.liste_royaume[0])
                        if result == "end":
                            self.reinitialiser_jeu()
                    elif self.jeu.victoire() == self.selection.liste_royaume[1]:
                        result = self.afficher_victoire(self.selection.liste_royaume[1])
                        if result == "end":
                            self.reinitialiser_jeu()

            # Mettre à jour l'affichage à chaque itération
            pygame.display.flip()
            pygame.display.update()

            # Limiter la boucle à 60 FPS
            pygame.time.Clock().tick(60)
            
            # Rétablir la forme de la souris par défaut
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def afficher_victoire(self, royaume):
        # Configuration de la fenêtre de victoire
        victoire_fenetre = pygame.display.set_mode(RESOLUTION_JEU)
        pygame.display.set_caption("Victoire")
        
        # Chargement du fond d'écran
        fond_victoire = pygame.image.load("assets/interface/main_menu_background.jpg")
        fond_victoire = pygame.transform.scale(fond_victoire, RESOLUTION_JEU)
        victoire_fenetre.blit(fond_victoire, (0, 0))
        
        # Chargement de l'image du bandeau
        bandeau_image = pygame.image.load("assets/interface/item_frame.png")
        bandeau_image = pygame.transform.scale(bandeau_image, (800, 100))  # Ajustez la taille du bandeau selon vos besoins
        
        # Position du bandeau (centré)
        bandeau_rect = bandeau_image.get_rect(center=(RESOLUTION_JEU[0] / 2, RESOLUTION_JEU[1] / 2))
        victoire_fenetre.blit(bandeau_image, bandeau_rect.topleft)
        
        # Texte de victoire
        font = pygame.font.Font(None, 50)
        text = font.render(f"Victoire : {royaume}", True, NOIR)
        text_rect = text.get_rect(center=(RESOLUTION_JEU[0] / 2, RESOLUTION_JEU[1] / 2))
        victoire_fenetre.blit(text, text_rect)
        
        # Mise à jour de l'affichage
        pygame.display.flip()
        pygame.display.update()
        
        # Pause de 5 secondes avant de retourner
        pygame.time.wait(5000)
        return "end"

    def reinitialiser_jeu(self):
        self.__init__()  # Réinitialiser l'état du jeu


if __name__ == "__main__":
    start = Main()
    start.boucle_principale()
