import pygame
from constante import *
from menu import Menu
from bouton import Bouton

class Selection:
    def __init__(self,fenetre):
        self.fenetre = fenetre  
        self.police = pygame.font.SysFont("Arial", 30)
    
        self.boutons = [Bouton("Royaume 1",50, 100, 200, 50),
                        Bouton("Royaume 2",300, 100, 200, 50),
                        Bouton("Royaume 3",550, 100, 200, 50),
                        Bouton("Suivant",300, 400, 200, 50)]
        
        self.royaumes_selectionnes = []

    def dessiner(self, fenetre):
        for i in self.boutons:
            i.afficher(fenetre)
        if len(self.royaumes_selectionnes) < 2:
            pygame.draw.rect(fenetre, (128, 128, 128), self.boutons[3].rect, 5) # Grisé le bouton
        for i, royaume in enumerate(self.royaumes_selectionnes):
            texte_royaume = self.police.render(royaume, True, NOIR)
            fenetre.blit(texte_royaume, (100, 450 + i * 30))

    def gerer_evenements(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boutons[0].rect.collidepoint(event.pos):
                if "Royaume 1" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Royaume 1")
                else:
                    self.royaumes_selectionnes.append("Royaume 1")
            elif self.boutons[1].rect.collidepoint(event.pos):
                if "Royaume 2" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Royaume 2")
                else:
                    self.royaumes_selectionnes.append("Royaume 2")
            elif self.boutons[2].rect.collidepoint(event.pos):
                if "Royaume 3" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Royaume 3")
                else:
                    self.royaumes_selectionnes.append("Royaume 3")
            elif self.boutons[3].rect.collidepoint(event.pos) and len(self.royaumes_selectionnes) == 2:
                return "jeu"
        return "selection"
    
    def get_royaumes_selectionnes(self):
        return self.royaumes_selectionnes