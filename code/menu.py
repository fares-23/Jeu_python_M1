import pygame
from bouton import Bouton
from constante import *

class Menu:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.image = [pygame.image.load("assets/interface/MenuButtonInactiv.png"),
                      pygame.image.load("assets/interface/MenuButtonPreLight.png")]
        self.boutons = [            
            Bouton("Start", self.fenetre.get_width() // 2 - 50, self.fenetre.get_height() // 2 - 80, 100, 50,NOIR,self.image[0],self.image[1]),
            Bouton("Quit", self.fenetre.get_width() // 2 - 50, self.fenetre.get_height() // 2 - 20, 100, 50,NOIR,self.image[0],self.image[1])
        ]

    def afficher(self):
        for bouton in self.boutons:
            bouton.afficher(self.fenetre)

    def verifier_clic(self, event):
        for bouton in self.boutons:
            if bouton.x < event.pos[0] < bouton.x + bouton.width and bouton.y < event.pos[1] < bouton.y + bouton.height:
                if bouton.text == "Start":
                    return "selection"
                elif bouton.text == "Quit":
                    pygame.quit()
                    sys.exit()
        return "menu"
    

