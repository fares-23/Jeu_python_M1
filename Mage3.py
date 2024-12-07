import pygame
from personnage import Personnage
from constante import *
import random

class Mage(Personnage):
    def __init__(self, x, y, royaume=None):
        super().__init__(x, y)
        self.image_path = mage_path
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 2
        self.esquive = 0.2
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

    # Compétences du Mage
    def boule_de_feu(self, cible):
        """Compétence 1 : Boule de Feu."""
        degats = (self.attaque * 2) - cible.defense
        cible.recevoir_attaque(max(degats, 0))
        print(f"{self.__class__.__name__} inflige {degats} dégâts à {cible.__class__.__name__} avec Boule de Feu.")

    def soigner(self, cible):
        """Compétence 2 : Soin."""
        soin = 20
        cible.pv = min(cible.pv + soin, 100)
        print(f"{self.__class__.__name__} soigne {cible.__class__.__name__}, qui récupère {soin} PV.")

    def explosion_magique(self, cibles):
        """Compétence 3 : Explosion Magique."""
        for cible in cibles:
            degats = (self.attaque * 1.5) - cible.defense
            cible.recevoir_attaque(max(degats, 0))
            print(f"{cible.__class__.__name__} perd {degats} PV.")

    def teleportation(self, x, y):
        """Compétence 4 : Téléportation."""
        self.rect.x = x
        self.rect.y = y
        print(f"{self.__class__.__name__} se téléporte à ({x}, {y}).")
