import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur

class Chevalier(Personnage):
    def __init__(self, x, y,image_path,royaume = None):
        super().__init__(x, y,image_path)  # Appelle le constructeur de Personnage
        self.image_path =  image_path 
        self.attaque = chevalier_attaque
        self.defense = chevalier_defense
        self.pv = chevalier_pv
        self.vitesse = chevalier_vitesse
        self.esquive = chevalier_esquive
        self.royaume = royaume
        self.action = True 
        self.nom = "chevalier"
        self.bandeau = BandeauInferieur()

    def competence(self,cible,fenetre):
        self.bandeau.afficher_message("'a' : Coup d'épée |'z' : Bouclier Divin  |'e' : Coup Puissant" ,fenetre)
        pygame.display.flip()
        choix = None
        self.action = False
        self.afficher_deplacement_possible = False
        while choix is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: # touche 1
                        choix = 1
                        degats = self.attaque - cible.defense
                        cible.recevoir_attaque(degats,fenetre)
                    if event.key == pygame.K_z:
                        choix = 2
                        self.buff(10,fenetre)
                    if event.key == pygame.K_e:
                        choix = 3
                        degats = 3*self.attaque - cible.defense
                        cible.recevoir_attaque(degats,fenetre)
                        
    def carte_effet(self):
        if (self.rect.x, self.rect.y) in self.boue:
            self.vitesse = 1
        elif (self.rect.x, self.rect.y) in self.arbre:
            self.esquive = 0.8
        else:
            self.vitesse = chevalier_vitesse
            self.esquive = chevalier_esquive