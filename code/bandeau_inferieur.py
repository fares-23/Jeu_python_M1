import pygame
from constante import *

class BandeauInferieur:
    def __init__(self):
        
        self.image = pygame.image.load("assets/interface/item_frame.png")
        self.image = pygame.transform.scale(self.image, (1200, 50))
        

        self.font = pygame.font.Font(None, 25)  # Police pour afficher les points de vie

    def afficher(self, fenetre):
        fenetre.blit(self.image, (0, 720))
        

    def afficher_personnage(self, fenetre,image_path,vie,attaque,defense):
        
        personnage_image = pygame.image.load(image_path)  # Remplacez par l'image de votre personnage
        personnage_image = pygame.transform.scale(personnage_image, (50, 50))  # Ajustez la taille de l'image
        
        fenetre.blit(personnage_image, (20, 720))  # Affiche l'image du personnage à la position (10, 725)
        vie_text = self.font.render(f"PV : {vie}", True, (0, 0, 0))  # Affiche les points de vie en noir
        fenetre.blit(vie_text, (90, 723))
        
        attaque_text = self.font.render(f"ATK : {attaque}", True, (0, 0, 0))  # Affiche les points de vie en noir
        fenetre.blit(attaque_text, (90, 738))
        
        defense_text = self.font.render(f"DEF : {defense}", True, (0, 0, 0))  # Affiche les points de vie en noir
        fenetre.blit(defense_text, (90, 753))

    def afficher_tour(self,fenetre,tour):
        tour_text = self.font.render(f"Tour du joueur  : {(tour%2)+1}", True, (0, 0, 0))
        fenetre.blit(tour_text, (1000, 735))
        
    def afficher_message(self,message,fenetre):
        self.afficher(fenetre)
        message_text = self.font.render(f"{message}", True, (0, 0, 0))
        fenetre.blit(message_text, (200, 735))
        pygame.display.flip()