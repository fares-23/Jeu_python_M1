import pygame
from constante import *
from menu import Menu
from bouton import Bouton
from empire_Adrastien import Empire_Adrastien
from saint_Royaume_de_Faerghus import Saint_Royaume_de_Faerghus
from alliance_de_Leicester import Alliance_de_Leicester


class Selection:
    def __init__(self, fenetre):
        self.fenetre = fenetre  
        self.police = pygame.font.SysFont("Arial", 30)
        self.image = [pygame.image.load("assets/interface/MenuButtonPreLight.png"),
                      pygame.image.load("assets/interface/item_frame.png")
                      ]

        
        self.boutons = [Bouton("Empire Adrastien",75, 100, 250, 50,NOIR,self.image[1]),
                        Bouton("Saint Royaume de Faerghus",375, 100, 400, 50,NOIR,self.image[1]),
                        Bouton("Alliance de Leicester",820, 100, 300, 50,NOIR,self.image[1]),
                        Bouton("Suivant",self.fenetre.get_width() // 2 - 100, self.fenetre.get_height() // 2 + 200, 200, 50,NOIR,self.image[0])]
        
        self.royaumes_selectionnes = []
        self.liste_troupe = []
        self.images =  [pygame.transform.smoothscale(pygame.image.load("assets/blason/Adrestian_crest.webp"), (200, 200)),
                        pygame.transform.smoothscale(pygame.image.load("assets/blason/Faerghus_crest.webp"), (200, 200)),
                        pygame.transform.smoothscale(pygame.image.load("assets/blason/Leicester_crest.webp"), (200, 200))]

        self.images_rect = [self.images[0].get_rect(topleft=(100, 200)), 
                            self.images[1].get_rect(topleft=(480, 200)), 
                            self.images[2].get_rect(topleft=(870, 200))]
        
    def dessiner(self, fenetre):
        for i in range(len(self.boutons)-1):
            self.boutons[i].afficher(fenetre)
        if len(self.royaumes_selectionnes) == 2:
            self.boutons[3].afficher(fenetre)
        for i, image in enumerate(self.images): # Affiche les images des royaumes
            if self.boutons[i].rect.collidepoint(pygame.mouse.get_pos()) or self.boutons[i].text in self.royaumes_selectionnes:
                fenetre.blit(image, self.images_rect[i])
    
    def gerer_evenements(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boutons[0].rect.collidepoint(event.pos):
                if "Empire Adrastien" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Empire Adrastien")
                else:
                    self.royaumes_selectionnes.append("Empire Adrastien")
            elif self.boutons[1].rect.collidepoint(event.pos):
                if "Saint Royaume de Faerghus" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Saint Royaume de Faerghus")
                else:
                    self.royaumes_selectionnes.append("Saint Royaume de Faerghus")
            elif self.boutons[2].rect.collidepoint(event.pos):
                if "Alliance de Leicester" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Alliance de Leicester")
                else:
                    self.royaumes_selectionnes.append("Alliance de Leicester")
                    
            elif self.boutons[3].rect.collidepoint(event.pos) and len(self.royaumes_selectionnes) == 2:
                for i in range(len(self.royaumes_selectionnes)):
                
                    if self.royaumes_selectionnes[i] == "Empire Adrastien":
                        self.royaumes_selectionnes[i] = Empire_Adrastien()
                        self.royaumes_selectionnes[i].armee(coordonnee_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                        
                    elif self.royaumes_selectionnes[i] == "Saint Royaume de Faerghus":
                        self.royaumes_selectionnes[i] = Saint_Royaume_de_Faerghus()
                        self.royaumes_selectionnes[i].armee(coordonnee_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                        
                    elif self.royaumes_selectionnes[i] == "Alliance de Leicester":
                        self.royaumes_selectionnes[i] = Alliance_de_Leicester()
                        self.royaumes_selectionnes[i].armee(coordonnee_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                return "jeu"
                    
        return "selection"
    