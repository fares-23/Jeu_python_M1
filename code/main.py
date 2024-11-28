import pygame
from personnage import Personnage
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from grille import Grille
from constante import *
import sys
from menu import Menu 
from bouton import Bouton
from jeu import Jeu

def main():
    pygame.init()
    fenetre = pygame.display.set_mode(RESOLUTION)
    menu = Menu(fenetre)
    jeu = Jeu()
    etat_jeu = "menu"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if etat_jeu == "menu":
                    etat_jeu = menu.verifier_clic(event)
                elif etat_jeu == "jeu":
                    jeu.verifier_clic(event)
            elif event.type == pygame.MOUSEMOTION:
                if etat_jeu == "menu":
                    for bouton in menu.boutons:
                        bouton.mettre_en_survol(fenetre, event)

        fenetre.fill(COULEUR_FOND)
        
        if etat_jeu == "menu":
            menu.afficher()
        elif etat_jeu == "jeu":
            jeu.afficher(fenetre)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
