import pygame
from personnage import Personnage
from constante import *
import random

class Chevalier(Personnage):
    def __init__(self, x, y, royaume=None):
        super().__init__(x, y)
        self.image_path = chevalier_path
        self.attaque = 10
        self.defense = 8
        self.pv = 120
        self.vitesse = 3
        self.esquive = 0.1
        self.royaume = royaume
        self.action = True

    def deplacement(self, grille, event, coordonnee):
        super().deplacement(grille, event, coordonnee)

    def afficher_deplacement(self, grille, fenetre, coordonnee):
        super().afficher_deplacement(grille, fenetre, coordonnee)

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)

    def recevoir_attaque(self, degats):
        if random.random() < self.esquive:
            print(f"{self.__class__.__name__} esquive l'attaque !")
        else:
            self.pv -= max(degats, 0)
            print(f"{self.__class__.__name__} reçoit {degats} dégâts !")

    # Compétences du Chevalier
    def coup_puissant(self, cible):
        """Compétence 1 : Coup Puissant."""
        degats = (self.attaque * 1.5) - cible.defense
        cible.recevoir_attaque(max(degats, 0))
        print(f"{self.__class__.__name__} inflige {degats} dégâts à {cible.__class__.__name__} avec Coup Puissant.")

    def protection(self, cibles):
        """Compétence 2 : Protection."""
        for cible in cibles:
            cible.defense += 5
            print(f"La défense de {cible.__class__.__name__} augmente temporairement.")

    def bouclier_divin(self):
        """Compétence 3 : Bouclier Divin."""
        print(f"{self.__class__.__name__} devient invincible pour un tour !")
        self.invincible = True

    def frappe_de_zone(self, cibles):
        """Compétence 4 : Frappe de Zone."""
        for cible in cibles:
            degats = max(10, self.attaque - cible.defense)
            cible.recevoir_attaque(degats)
            print(f"{cible.__class__.__name__} perd {degats} PV.")

