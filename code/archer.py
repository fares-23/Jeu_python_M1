import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur
class Archer(Personnage):
    def __init__(self, x, y,image_path,royaume = None):
        super().__init__(x, y,image_path)  # Appelle le constructeur de Personnage
        self.image_path = image_path
        self.attaque = archer_attaque
        self.defense = archer_defense
        self.pv = archer_pv
        self.vitesse = archer_vitesse 
        self.esquive = archer_esquive
        self.nom = "archer"
        self.royaume = royaume
        self.action = True
    

    
    def competence(self,cible,fenetre):
        self.bandeau.afficher_message("'a' : Tir simple |'z' : Tir puissant | 'e' : Attaque rapide" ,fenetre)
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
                        degats = 3*self.attaque - cible.defense
                        cible.recevoir_attaque(degats,fenetre)
                    if event.key == pygame.K_e:
                        choix = 3
                        for i in range(2):  # Deux attaques rapides
                            print("Attaque rapide !")
                            degats = self.attaque - cible.defense
                        cible.recevoir_attaque(2*degats,fenetre)
                        
    def carte_effet(self):
        if (self.rect.x, self.rect.y) in self.boue:
            self.vitesse = 1
        elif (self.rect.x, self.rect.y) in self.arbre:
            self.esquive = 0.8
        else:
            self.vitesse = archer_vitesse
            self.esquive = archer_esquive