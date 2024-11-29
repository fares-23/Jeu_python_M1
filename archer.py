import pygame
from personnage import Personnage

class Archer(Personnage):
    def __init__(self, x, y, couleur_perso):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.couleur_perso = couleur_perso  # Redéfini pour l'archer
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 4  # Vitesse spécifique à l'archer
        self.esquive = 0.3

    def deplacement(self, grille, event, coordonnee):
        super().deplacement(grille, event, coordonnee)
    
    def afficher_deplacement(self, grille, fenetre, coordonnee):
        super().afficher_deplacement(grille, fenetre, coordonnee) 

    def afficher_personnage(self, fenetre): 
        super().afficher_personnage(fenetre)
        
    def tir_precis(self, cible):
         """Compétence 1 : Tir précis."""
         degats = self.attaque - cible.defense
         if degats > 0:
          cible.pv -= degats
         print(f"L'Archer inflige {degats} dégâts à {cible.__class__.__name__}.")

    def pluie_de_fleches(self, cibles):
        """Compétence 2 : Pluie de flèches (attaque de zone)."""
        print("L'Archer utilise Pluie de Flèches !")
        for cible in cibles:
            degats = max(5, self.attaque // 2 - cible.defense)
            cible.pv -= degats
            print(f"{cible.__class__.__name__} perd {degats} PV.")

    def tir_empoisonne(self, cible):
        """Compétence 3 : Tir Empoisonné."""
        degats = self.attaque - cible.defense
        if degats > 0:
            cible.pv -= degats
            cible.etat = "empoisonné"
            print(f"L'Archer empoisonne {cible.__class__.__name__}, infligeant {degats} dégâts initiaux.")

    def tir_rapide(self, cible):
        """Compétence 4 : Tir Rapide."""
        print("L'Archer utilise Tir Rapide !")
        for _ in range(2):  # Tire deux fois
            degats = self.attaque - cible.defense
            if degats > 0:
                cible.pv -= degats
                print(f"L'Archer inflige {degats} dégâts à {cible.__class__.__name__}.")