 
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
   #musique
    
    #pygame.mixer.music.load("assets/music/FE Three Houses OST - 4. The Edge of Dawn (Seasons of Warfare) (English).mp3")
    #pygame.mixer.music.play(start=0.0, fade_ms=5000)
    pygame.mixer.music.set_volume(0.5)

    def __init__(self):
        # Initialisation de la fenêtre Pygame
        self.fenetre = pygame.display.set_mode(RESOLUTION_JEU)
        pygame.display.set_caption("Jeu avec Tiled")

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
        # État initial
        self.etat = "menu"

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
                                self.jeu.combat(perso,self.fenetre)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.etat == "menu":
                        self.etat = self.menu.verifier_clic(event)
                    elif self.etat == "selection":
                        self.etat = self.selection.gerer_evenements(event,self.coord_start)
                    elif self.etat == "jeu":
                        self.jeu.verifier_clic(event,self.carte, self.selection.liste_royaume)
                        
            self.jeu.liste_personnage = self.selection.liste_troupe

         
            # Remplir l'écran avec une couleur de fond
            #self.fenetre.fill(BLANC)  # Fond blanc pour vérifier l'affichage
            self.fenetre.blit(self.fond,(0, 0))  # Dessinez l'image de fond
            # Afficher la carte TMX à l'écran (utilisation de Grille pour la gestion des cases)
            
            # Afficher le contenu en fonction de l'état actuel du jeu
            if self.etat == "menu":
                self.menu.afficher()
            elif self.etat == "selection":
                self.selection.dessiner(self.fenetre)
            elif self.etat == "jeu":
                self.carte.afficher(self.fenetre)  # Affiche la carte
                self.jeu.afficher(self.fenetre, self.carte.tmx_data,self.carte,self.selection.liste_royaume)
                
                

             # Mettre à jour l'affichage à chaque itération
            pygame.display.flip()
            pygame.display.update()

            # Limiter la boucle à 60 FPS
            pygame.time.Clock().tick(60)
            
            # Rétablir la forme de la souris par défaut
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

 
if __name__ == "__main__":
    start = Main()
    start.boucle_principale()

