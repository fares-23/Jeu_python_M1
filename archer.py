import pygame
from personnage import Personnage
from constante import *
import random

class Archer(Personnage):
    def __init__(self, x, y, royaume=None):
        super().__init__(x, y)
        self.image_path = archer_path
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 4
        self.esquive = 0.3
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

    # Compétences de l'Archer
    def tir_precis(self, cible):
        """Compétence 1 : Tir Précis."""
        degats = self.attaque - cible.defense
        cible.recevoir_attaque(max(degats, 0))
        print(f"{self.__class__.__name__} inflige {degats} dégâts à {cible.__class__.__name__} avec Tir Précis.")

    def pluie_de_fleches(self, cibles):
        """Compétence 2 : Pluie de Flèches."""
        for cible in cibles:
            degats = max(5, self.attaque // 2 - cible.defense)
            cible.recevoir_attaque(degats)
            print(f"{cible.__class__.__name__} perd {degats} PV.")

    def tir_empoisonne(self, cible):
        """Compétence 3 : Tir Empoisonné."""
        degats = self.attaque - cible.defense
        cible.recevoir_attaque(max(degats, 0))
        cible.etat = "empoisonné"
        print(f"{cible.__class__.__name__} est maintenant empoisonné.")

    def tir_rapide(self, cible):
        """Compétence 4 : Tir Rapide."""
        for _ in range(2):
            degats = self.attaque - cible.defense
            cible.recevoir_attaque(max(degats, 0))
            print(f"{self.__class__.__name__} inflige {degats} dégâts à {cible.__class__.__name__}.")

