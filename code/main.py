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
    
    #musique
    #pygame.mixer.init()
    #pygame.mixer.music.load("assets/music/FE Three Houses OST - 4. The Edge of Dawn (Seasons of Warfare) (English).mp3")
    #pygame.mixer.music.play(loops=-1,start=0.0, fade_ms=5000)

    def __init__(self):
        # Initialisation de la fenêtre Pygame
        self.fenetre = pygame.display.set_mode(RESOLUTION_JEU)
        pygame.display.set_caption("Jeu avec Tiled")

        # Charger la carte TMX
        try:
            self.tmx_data = load_pygame("map.tmx")
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
        self.fond = pygame.image.load("assets/interface/main_menu_background.jpg")  # Remplacez par le chemin vers votre image
        self.fond = pygame.transform.scale(self.fond, RESOLUTION_JEU)  # Redimensionnez l'image en fonction de la taille de la fenêtre
        
        # Initialisation de l'état du jeu (menu au départ)
        self.etat = "menu"
        
    def boucle_principale(self):
        # Définition de la police de caractères et de la taille du texte
        police = pygame.font.SysFont("Arial", 24)
        # Définition du texte à afficher
        texte = "Votre texte ici"
        surface_texte = police.render(texte, True, (0, 0, 0))  # Noir
        # Définition de la position du texte
        x = 0  # Vous pouvez ajuster cette valeur pour déplacer le texte horizontalement
        y = 720  # Vous avez spécifié cette valeur
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.etat == "menu":
                        self.etat = self.menu.verifier_clic(event)
                    elif self.etat == "selection":
                        self.etat = self.selection.gerer_evenements(event)
                    elif self.etat == "jeu":
                        self.jeu.verifier_clic(event,self.selection.liste_royaume)
                        
            self.jeu.liste_personnage = self.selection.liste_troupe

            # Remplir l'écran avec une couleur de fond
            #self.fenetre.fill(BLANC)  # Fond blanc pour vérifier l'affichage
            self.fenetre.blit(self.fond)  # Dessinez l'image de fond
            # Afficher la carte TMX à l'écran (utilisation de Grille pour la gestion des cases)
            
            

            # Afficher le contenu en fonction de l'état actuel du jeu
            if self.etat == "menu":
                self.menu.afficher()
            elif self.etat == "selection":
                self.selection.dessiner(self.fenetre)
            elif self.etat == "jeu":
                self.fenetre.fill(BLANC)
                self.fenetre.blit(surface_texte, (x, y))
                self.jeu.afficher(self.fenetre,self.tmx_data)
                

            # Mettre à jour l'affichage à chaque itération
            pygame.display.flip()
            pygame.display.update()

            # Limiter la boucle à 60 FPS
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    start = Main()
    start.boucle_principale()
