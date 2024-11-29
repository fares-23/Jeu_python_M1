import pygame
from constante import *
import sys
from menu import Menu 
from bouton import Bouton
from jeu import Jeu
from selection import Selection

class Main():
    pygame.init()
    def __init__(self):
        self.fenetre = pygame.display.set_mode(RESOLUTION)
        self.menu = Menu(self.fenetre)
        self.selection = Selection(self.fenetre)
        self.jeu = Jeu()
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

            self.fenetre.fill(BLANC)

            if self.etat == "menu":
                self.menu.afficher()
            elif self.etat == "selection":
                self.selection.dessiner(self.fenetre)
            elif self.etat == "jeu":
                self.jeu.afficher(self.fenetre)

            pygame.display.flip()
            pygame.display.update()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    start = Main()
    start.boucle_principale()
