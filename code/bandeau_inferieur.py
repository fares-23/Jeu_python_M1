import pygame
from constante import *


class BandeauInferieur:
    def __init__(self):
        self.image = pygame.image.load("assets/interface/item_frame.png")
        self.image = pygame.transform.scale(self.image, (1200, 50))

    def afficher(self,fenetre):
        fenetre.blit(self.image, (0, 720))
        