import pygame
from constante import *

class BandeauInferieur:
    def __init__(self):
        
        self.image = pygame.image.load("assets/interface/item_frame.png")
        self.image = pygame.transform.scale(self.image, (1200, 50))
        

        self.font = pygame.font.Font(None, 36)  # Police pour afficher les points de vie

    def afficher(self, fenetre):
        fenetre.blit(self.image, (0, 720))
        

    def afficher_personnage(self, fenetre,image_path,vie):
        
        personnage_image = pygame.image.load(image_path)  # Remplacez par l'image de votre personnage
        personnage_image = pygame.transform.scale(personnage_image, (50, 50))  # Ajustez la taille de l'image
        
        fenetre.blit(personnage_image, (10, 725))  # Affiche l'image du personnage à la position (10, 725)
        vie_text = self.font.render(f"PV : {vie}", True, (0, 0, 0))  # Affiche les points de vie en noir
        fenetre.blit(vie_text, (70, 730))

