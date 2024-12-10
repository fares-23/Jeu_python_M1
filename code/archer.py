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
        self.nb_tir_puissant = 3
        self.nb_attaque_rapide = 5

    
    def competence(self,cible,fenetre):
        self.bandeau.afficher_message(f"'a' : Tir simple |'z' : Tir puissant ({self.nb_tir_puissant})| 'e' : Attaque rapide ({self.nb_attaque_rapide})" ,fenetre)
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
                        if self.nb_tir_puissant > 0:
                            self.nb_tir_puissant -= 1
                            degats = 3*self.attaque - cible.defense
                            cible.recevoir_attaque(degats,fenetre)
                        else:
                            self.bandeau.afficher_message("Vous n'avez plus de tir puissant",fenetre)
                            pygame.time.wait(500)
                            self.action = True
                    if event.key == pygame.K_e:
                        choix = 3
                        if self.nb_attaque_rapide > 0:
                            for i in range(2):  # Deux attaques rapides
                                degats = self.attaque - cible.defense
                            cible.recevoir_attaque(2*degats,fenetre)
                            self.nb_attaque_rapide -= 1
                        else:
                            self.bandeau.afficher_message("Vous n'avez plus d'attaque rapide",fenetre)
                            pygame.time.wait(500)
                            self.action = True
                        
    def carte_effet(self):
        if (self.rect.x, self.rect.y) in self.boue:
            self.vitesse = 1
        elif (self.rect.x, self.rect.y) in self.arbre:
            self.esquive = 0.8
        else:
            self.vitesse = archer_vitesse
            self.esquive = archer_esquive