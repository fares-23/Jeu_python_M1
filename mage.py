import random
import pygame
from personnage import Personnage

class Mage(Personnage):
    def __init__(self, x, y, couleur_perso):
        super().__init__(x, y)
        self.couleur_perso = couleur_perso
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 2
        self.esquive = 0.2  # 20% de chance d'esquiver une attaque

    def deplacement(self, grille, event, coordonnee):
        super().deplacement(grille, event, coordonnee)
    
    def afficher_deplacement(self, grille, fenetre, coordonnee):
        super().afficher_deplacement(grille, fenetre, coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)

    def recevoir_attaque(self, degats):
        """Gère les dégâts reçus en tenant compte de l'esquive."""
        if random.random() < self.esquive:
            print(f"{self.__class__.__name__} esquive l'attaque !")
        else:
            self.pv -= max(degats, 0)
            print(f"{self.__class__.__name__} reçoit {degats} dégâts !")

    def utiliser_competence(self, cible):
        """Compétence 1 : Boule de Feu."""
        degats = (self.attaque * 2) - cible.defense
        if degats > 0:
            cible.recevoir_attaque(degats)
        print(f"Le Mage inflige {degats} dégâts à {cible.__class__.__name__} avec Boule de Feu.")

    def soigner(self, cible):
        """Compétence 2 : Soin."""
        soin = 20
        cible.pv += soin
        print(f"Le Mage soigne {cible.__class__.__name__}, qui récupère {soin} PV.")

    def explosion_magique(self, cibles):
        """Compétence 3 : Explosion Magique."""
        print("Le Mage utilise Explosion Magique !")
        for cible in cibles:
            degats = (self.attaque * 1.5) - cible.defense
            if degats > 0:
                cible.recevoir_attaque(degats)
                print(f"{cible.__class__.__name__} perd {degats} PV.")

    def teleportation(self, x, y):
        """Compétence 4 : Téléportation."""
        print(f"Le Mage se téléporte de ({self.x}, {self.y}) à ({x}, {y}).")
        self.x = x
        self.y = y
"""
Le Mage : Esquive à 20%
Rôle : Le Mage est un personnage de soutien et d’attaque magique, plus fragile que le Chevalier.

Pourquoi 20% ?

Le Mage est un personnage intermédiaire : ni aussi agile que l’Archer, ni aussi résistant que le Chevalier.
Avec 20% d’esquive, il a une chance modérée d’éviter les attaques, mais sa survie repose davantage sur sa capacité à rester hors de portée et à utiliser ses compétences.
Caractéristique : Polyvalent avec des capacités défensives (soin, téléportation) et offensives (attaques magiques).
Impact stratégique :

Le joueur doit jouer prudemment, utiliser le soin pour régénérer des PV ou se téléporter pour échapper au danger.
L’esquive à 20% reflète un équilibre entre fragilité et flexibilité.
"""