import pygame
from personnage import Personnage

class Mage(Personnage):
    def __init__(self, x, y,couleur_perso):
        super().__init__(x, y) 
        self.couleur_perso = couleur_perso 
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 2 

    def deplacement(self,grille,event,coordonnee):
        super().deplacement(grille,event,coordonnee)
    
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        super().afficher_deplacement(grille,fenetre,coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)
    def utiliser_competence(self, cible):
        """Compétence 1 : Boule de Feu. """
        degats = (self.attaque * 2) - cible.defense
        if degats > 0:
            cible.pv -= degats
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
                cible.pv -= degats
                print(f"{cible.__class__.__name__} perd {degats} PV.")

    def teleportation(self, x, y):
        """Compétence 4 : Téléportation."""
        print(f"Le Mage se téléporte de ({self.x}, {self.y}) à ({x}, {y}).")
        self.x = x
        self.y = y    