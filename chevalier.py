import pygame
from personnage import Personnage

class Chevalier(Personnage):
    def __init__(self, x, y,couleur_perso):
        super().__init__(x, y)  # Appelle le constructeur de Personnage
        self.couleur_perso = couleur_perso  # Redéfini pour l'archer
        self.attaque = 10
        self.defense = 5
        self.pv = 100
        self.vitesse = 3  # Vitesse spécifique à l'archer

    def deplacement(self,grille,event,coordonnee):
        super().deplacement(grille,event,coordonnee)
    
    def afficher_deplacement(self, grille,fenetre,coordonnee):
        super().afficher_deplacement(grille,fenetre,coordonnee) 

    def afficher_personnage(self, fenetre):
        super().afficher_personnage(fenetre)
    def utiliser_competence(self, cible):
         """Compétence 1 : Coup Puissant."""
         degats = (self.attaque * 1.5) - cible.defense
         if degats > 0:
             cible.pv -= degats
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
             cible.pv -= degats
             print(f"{cible.__class__.__name__} perd {degats} PV.")
    