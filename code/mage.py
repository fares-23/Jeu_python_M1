import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur

class Mage(Personnage):
    def __init__(self, x, y,image_path,royaume = None):
        super().__init__(x, y,image_path) 
        self.image_path =  image_path 
        self.attaque = mage_attaque
        self.defense = mage_defense
        self.pv = mage_pv
        self.vitesse = mage_vitesse 
        self.esquive = mage_esquive
        self.royaume = royaume
        self.action = True
        self.nom = "mage"
        self.bandeau = BandeauInferieur()
        self.nb_soin = 5
        self.nb_explosion = 3
        
    def competence(self,cible,fenetre):
        self.bandeau.afficher_message(f"'a' : Boule de Feu |'z' : Soin ({self.nb_soin}) |'e' : Explosion Magique ({self.nb_explosion})" ,fenetre)
        pygame.display.flip()
        choix = None
        self.action = False
        self.afficher_deplacement_possible = False
        while choix is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        choix = 1
                        degats = self.attaque - cible.defense
                        cible.recevoir_attaque(degats,fenetre)
                    if event.key == pygame.K_z:
                        choix = 2
                        if self.nb_soin > 0:
                            self.nb_soin -= 1
                            self.soigner(20,fenetre)
                        else:
                            self.action = True
                            self.bandeau.afficher_message("Vous n'avez plus de soin",fenetre)
                            pygame.time.wait(500)
                    if event.key == pygame.K_e:
                        choix = 3
                        if self.nb_explosion > 0:
                            self.nb_explosion -= 1
                            degats = 3*self.attaque - cible.defense
                            cible.recevoir_attaque(degats,fenetre)
                        else:
                            self.action = True
                            self.bandeau.afficher_message("Vous n'avez plus d'explosion mage",fenetre)
                            pygame.time.wait(500)
    def carte_effet(self):
        if (self.rect.x, self.rect.y) in self.boue:
            self.vitesse = 1
        elif (self.rect.x, self.rect.y) in self.arbre:
            self.esquive = 0.8
        else:
            self.vitesse = mage_vitesse
            self.esquive = mage_esquive