import random
import pygame
from personnage import Personnage

class Chevalier(Personnage):
    def __init__(self, x, y, couleur_perso):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.couleur_perso = couleur_perso  # Couleur du personnage
        self.attaque = 10
        self.defense = 8  # Meilleure défense
        self.pv = 120  # Plus de PV
        self.vitesse = 3
        self.esquive = 0.1  # 10% de chance d'esquiver une attaque

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
        """Compétence 1 : Coup Puissant."""
        degats = (self.attaque * 1.5) - cible.defense
        if degats > 0:
            cible.recevoir_attaque(degats)
        print(f"Le Chevalier inflige {degats} dégâts à {cible.__class__.__name__} avec Coup Puissant.")

    def protection(self, cibles):
        """Compétence 2 : Protection."""
        print("Le Chevalier utilise Protection pour réduire les dégâts des alliés.")
        for cible in cibles:
            cible.defense += 5
            print(f"La défense de {cible.__class__.__name__} augmente temporairement.")

    def bouclier_divin(self):
        """Compétence 3 : Bouclier Divin."""
        print("Le Chevalier devient temporairement invincible !")
        self.invincible = True  # Nouvel attribut temporaire pour l'invincibilité

    def frappe_de_zone(self, cibles):
        """Compétence 4 : Frappe de Zone."""
        print("Le Chevalier utilise Frappe de Zone !")
        for cible in cibles:
            degats = max(10, self.attaque - cible.defense)
            cible.recevoir_attaque(degats)
            print(f"{cible.__class__.__name__} perd {degats} PV.")
"""
 Le Chevalier : Esquive à 10%
Rôle : Le Chevalier est un tank, conçu pour absorber les attaques grâce à sa haute défense et ses PV élevés.

Pourquoi 10% ?

Le Chevalier n’a pas besoin de beaucoup esquiver puisqu'il est conçu pour encaisser les coups.
Son rôle principal est de protéger ses alliés et d’attaquer les ennemis au corps-à-corps.
Caractéristique : Peu mobile et agile, mais très résistant.
Impact stratégique :

Le joueur peut prendre des risques avec le Chevalier en l’envoyant au cœur de la mêlée.
Avec une esquive de 10%, il a une petite chance d’éviter les dégâts, mais sa survie repose avant tout sur ses PV élevés et ses compétences de protection.
"""