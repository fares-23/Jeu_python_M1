import random
import pygame
from personnage import Personnage

class Archer(Personnage):
    def __init__(self, x, y, couleur_perso):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.couleur_perso = couleur_perso  # Couleur du personnage
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 4  # Vitesse spécifique à l'archer
        self.esquive = 0.3  # 30% de chance d'esquiver une attaque

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
        
    def tir_precis(self, cible):
        """Compétence 1 : Tir précis."""
        degats = self.attaque - cible.defense
        if degats > 0:
            cible.recevoir_attaque(degats)
        print(f"L'Archer inflige {degats} dégâts à {cible.__class__.__name__}.")

    def pluie_de_fleches(self, cibles):
        """Compétence 2 : Pluie de flèches (attaque de zone)."""
        print("L'Archer utilise Pluie de Flèches !")
        for cible in cibles:
            degats = max(5, self.attaque // 2 - cible.defense)
            cible.recevoir_attaque(degats)
            print(f"{cible.__class__.__name__} perd {degats} PV.")

    def tir_empoisonne(self, cible):
        """Compétence 3 : Tir Empoisonné."""
        degats = self.attaque - cible.defense
        if degats > 0:
            cible.recevoir_attaque(degats)
            cible.etat = "empoisonné"
            print(f"L'Archer empoisonne {cible.__class__.__name__}, infligeant {degats} dégâts initiaux.")

    def tir_rapide(self, cible):
        """Compétence 4 : Tir Rapide."""
        print("L'Archer utilise Tir Rapide !")
        for _ in range(2):  # Tire deux fois
            degats = self.attaque - cible.defense
            if degats > 0:
                cible.recevoir_attaque(degats)
                print(f"L'Archer inflige {degats} dégâts à {cible.__class__.__name__}.")
"""
1. L'Archer : Esquive à 30%
Rôle : L'Archer est un combattant à distance, rapide et agile.

Pourquoi 30% ?

L'archer compense sa relative fragilité (faibles PV et défense) par une grande capacité à éviter les attaques.
Cela reflète son agilité et sa capacité à esquiver facilement les attaques ennemies.
Caractéristique : Grande vitesse et esquive élevée, mais faible résistance en cas de coup reçu.
Impact stratégique :

Le joueur est encouragé à garder l'Archer à distance des ennemis tout en profitant de sa mobilité.
Avec 30% d'esquive, l'Archer a près d'une chance sur trois d'éviter les dégâts.
"""