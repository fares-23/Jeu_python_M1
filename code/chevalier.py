import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur

# Définition de la classe Chevalier, qui hérite de la classe abstraite Personnage
class Chevalier(Personnage):
    def __init__(self, x, y, image_path, royaume=None):
        """
        Constructeur de la classe Chevalier.
        :param x: Coordonnée x initiale du chevalier.
        :param y: Coordonnée y initiale du chevalier.
        :param image_path: Chemin vers l'image représentant le chevalier.
        :param royaume: Nom du royaume auquel appartient le chevalier.
        """
        super().__init__(x, y, image_path)  # Appelle le constructeur de la classe parent Personnage

        # Initialisation des attributs spécifiques au Chevalier
        self.image_path = image_path  # Chemin de l'image associée au chevalier
        self.attaque = chevalier_attaque  # Valeur d'attaque du chevalier
        self.defense = chevalier_defense  # Valeur de défense du chevalier
        self.pv = chevalier_pv  # Points de vie du chevalier
        self.vitesse = chevalier_vitesse  # Vitesse de déplacement du chevalier
        self.esquive = chevalier_esquive  # Probabilité d'esquiver une attaque
        self.royaume = royaume  # Royaume auquel appartient le chevalier
        self.action = True  # Indique si le chevalier peut encore agir ce tour
        self.nom = "chevalier"  # Nom de l'unité
        self.bandeau = BandeauInferieur()  # Instance pour afficher les messages
        self.nb_bouclier_divin = 1  # Nombre de boucliers divins disponibles
        self.nb_coup_puissant = 3  # Nombre de coups puissants disponibles

    # Méthode pour gérer les compétences spécifiques du Chevalier
    def competence(self, cible, fenetre):
        """
        Permet au chevalier d'utiliser une compétence sur une cible.
        :param cible: L'unité cible de l'attaque ou de l'effet.
        :param fenetre: La fenêtre Pygame où les messages et effets sont affichés.
        """
        # Affiche les options de compétences disponibles
        self.bandeau.afficher_message(f"'a' : Coup d'épée |'z' : Bouclier Divin ({self.nb_bouclier_divin})  |'e' : Coup Puissant ({self.nb_coup_puissant})" ,fenetre)
        pygame.display.flip()  # Met à jour l'affichage

        choix = None  # Variable pour stocker le choix du joueur
        self.action = False  # Désactive d'autres actions en cours
        self.afficher_deplacement_possible = False  # Désactive l'affichage des déplacements

        # Boucle pour attendre une entrée utilisateur
        while choix is None:
            for event in pygame.event.get():  # Parcourt les événements
                if event.type == pygame.KEYDOWN:  # Si une touche est pressée
                    if event.key == pygame.K_a:  # Coup d'épée
                        choix = 1
                        degats = self.attaque - cible.defense  # Calcule les dégâts infligés
                        cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts à la cible
                    if event.key == pygame.K_z:  # Bouclier divin
                        choix = 2
                        if self.nb_bouclier_divin > 0:  # Vérifie si des boucliers divins sont disponibles
                            self.nb_bouclier_divin -= 1  # Diminue le compteur de boucliers divins
                            self.buff(10, fenetre)  # Augmente la défense du chevalier
                        else:
                            self.action = True  # Réactive l'action si aucune compétence n'est utilisée
                            self.bandeau.afficher_message("Vous n'avez plus de bouclier divin", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message
                    if event.key == pygame.K_e:  # Coup puissant
                        choix = 3
                        if self.nb_coup_puissant > 0:  # Vérifie si des coups puissants sont disponibles
                            self.nb_coup_puissant -= 1  # Diminue le compteur de coups puissants
                            degats = 3 * self.attaque - cible.defense  # Calcule les dégâts infligés
                            cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts
                        else:
                            self.action = True  # Réactive l'action si aucune compétence n'est utilisée
                            self.bandeau.afficher_message("Vous n'avez plus de coup puissant", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message

    # Méthode pour gérer les effets des cases spéciales sur le chevalier
    def carte_effet(self):
        """
        Applique les effets des cases spéciales sur le chevalier (ralentissement, augmentation d'esquive, etc.).
        """
        if (self.rect.x, self.rect.y) in self.boue:  # Si le chevalier est sur une case de boue
            self.vitesse = 1  # Réduit sa vitesse
        elif (self.rect.x, self.rect.y) in self.arbre:  # Si le chevalier est sur une case d'arbre
            self.esquive = 0.8  # Augmente son esquive
        else:
            # Réinitialise les valeurs par défaut si aucune condition spéciale n'est remplie
            self.vitesse = chevalier_vitesse
            self.esquive = chevalier_esquive
