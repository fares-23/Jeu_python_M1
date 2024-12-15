import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur

# Définition de la classe Archer, héritant de la classe Personnage
class Archer(Personnage):
    def __init__(self, x, y, image_path, royaume=None):
        # Appelle le constructeur de la classe parent Personnage
        super().__init__(x, y, image_path)
        
        # Initialisation des attributs spécifiques à l'Archer
        self.image_path = image_path  # Chemin de l'image associée à l'Archer
        self.attaque = archer_attaque  # Valeur d'attaque de l'Archer
        self.defense = archer_defense  # Valeur de défense de l'Archer
        self.pv = archer_pv  # Points de vie de l'Archer
        self.vitesse = archer_vitesse  # Vitesse de déplacement
        self.esquive = archer_esquive  # Probabilité d'esquiver une attaque
        self.nom = "archer"  # Nom de l'unité
        self.royaume = royaume  # Royaume auquel appartient l'Archer
        self.action = True  # Statut indiquant si l'Archer peut encore agir ce tour
        self.nb_tir_puissant = 3  # Nombre de tirs puissants restants
        self.nb_attaque_rapide = 5  # Nombre d'attaques rapides restantes

    # Méthode pour gérer les compétences spécifiques de l'Archer
    def competence(self, cible, fenetre):
        # Affiche les options de compétences disponibles
        self.bandeau.afficher_message(f"'a' : Tir simple |'z' : Tir puissant ({self.nb_tir_puissant})| 'e' : Attaque rapide ({self.nb_attaque_rapide})" ,fenetre)
        pygame.display.flip()  # Met à jour l'affichage
        
        choix = None  # Variable pour stocker le choix du joueur
        self.action = False  # Empêche d'autres actions simultanées
        self.afficher_deplacement_possible = False  # Désactive l'affichage des déplacements
        
        # Boucle pour attendre une entrée utilisateur
        while choix is None:
            for event in pygame.event.get():  # Parcourt tous les événements
                if event.type == pygame.KEYDOWN:  # Si une touche est pressée
                    if event.key == pygame.K_a:  # Tir simple
                        choix = 1
                        degats = self.attaque - cible.defense  # Calcule les dégâts
                        cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts à la cible
                    if event.key == pygame.K_z:  # Tir puissant
                        choix = 2
                        if self.nb_tir_puissant > 0:  # Vérifie si des tirs puissants sont disponibles
                            self.nb_tir_puissant -= 1  # Diminue le compteur de tirs puissants
                            degats = 3 * self.attaque - cible.defense  # Calcule les dégâts
                            cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts
                        else:
                            # Affiche un message d'erreur si les tirs puissants sont épuisés
                            self.bandeau.afficher_message("Vous n'avez plus de tir puissant", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message
                            self.action = True  # Réactive l'action
                    if event.key == pygame.K_e:  # Attaque rapide
                        choix = 3
                        if self.nb_attaque_rapide > 0:  # Vérifie si des attaques rapides sont disponibles
                            for i in range(2):  # Effectue deux attaques rapides
                                degats = self.attaque - cible.defense  # Calcule les dégâts
                            cible.recevoir_attaque(2 * degats, fenetre)  # Applique les dégâts
                            self.nb_attaque_rapide -= 1  # Diminue le compteur d'attaques rapides
                        else:
                            # Affiche un message d'erreur si les attaques rapides sont épuisées
                            self.bandeau.afficher_message("Vous n'avez plus d'attaque rapide", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message
                            self.action = True  # Réactive l'action

    # Méthode pour gérer les effets des cases spéciales
    def carte_effet(self):
        # Si l'Archer est sur une case de boue, sa vitesse est réduite
        if (self.rect.x, self.rect.y) in self.boue:
            self.vitesse = 1
        # Si l'Archer est sur une case d'arbre, son esquive augmente
        elif (self.rect.x, self.rect.y) in self.arbre:
            self.esquive = 0.8
        # Sinon, ses attributs reprennent leurs valeurs de base
        else:
            self.vitesse = archer_vitesse
            self.esquive = archer_esquive
