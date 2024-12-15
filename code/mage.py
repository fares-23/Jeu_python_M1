import pygame
from personnage import Personnage
from constante import *
from bandeau_inferieur import BandeauInferieur

# Définition de la classe Mage, qui hérite de la classe abstraite Personnage
class Mage(Personnage):
    def __init__(self, x, y, image_path, royaume=None):
        """
        Constructeur de la classe Mage.
        Initialise les attributs spécifiques au personnage Mage.
        :param x: Position initiale en x.
        :param y: Position initiale en y.
        :param image_path: Chemin vers l'image représentant le Mage.
        :param royaume: Nom du royaume auquel appartient le Mage.
        """
        super().__init__(x, y, image_path)  # Appelle le constructeur de la classe parent

        # Initialisation des attributs spécifiques au Mage
        self.image_path = image_path  # Chemin de l'image associée au Mage
        self.attaque = mage_attaque  # Valeur d'attaque du Mage
        self.defense = mage_defense  # Valeur de défense du Mage
        self.pv = mage_pv  # Points de vie du Mage
        self.vitesse = mage_vitesse  # Vitesse de déplacement du Mage
        self.esquive = mage_esquive  # Probabilité d'esquiver une attaque
        self.royaume = royaume  # Royaume auquel appartient le Mage
        self.action = True  # Indique si le Mage peut encore agir ce tour
        self.nom = "mage"  # Nom de l'unité (utilisé pour les messages et affichages)
        self.bandeau = BandeauInferieur()  # Instance pour afficher les messages et informations

        # Compteurs pour les compétences spéciales du Mage
        self.nb_soin = 5  # Nombre de sorts de soin disponibles
        self.nb_explosion = 3  # Nombre de sorts d'explosion magique disponibles

    def competence(self, cible, fenetre):
        """
        Gère l'utilisation des compétences spécifiques du Mage.
        :param cible: La cible de l'attaque ou du sort.
        :param fenetre: La fenêtre où les messages et animations sont affichés.
        """
        # Affiche les options de compétences disponibles pour le Mage
        
        self.bandeau.afficher_message(f"'a' : Boule de Feu |'z' : Soin ({self.nb_soin}) |'e' : Explosion Magique ({self.nb_explosion})" ,fenetre)
        pygame.display.flip()  # Met à jour l'affichage

        # Variables de contrôle pour attendre l'entrée utilisateur
        choix = None
        self.action = False  # Désactive les autres actions pendant le choix
        self.afficher_deplacement_possible = False  # Désactive l'affichage des déplacements

        # Boucle pour attendre un choix de compétence
        while choix is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Vérifie si une touche est pressée
                    if event.key == pygame.K_a:  # Boule de Feu
                        choix = 1
                        degats = self.attaque - cible.defense  # Calcule les dégâts infligés
                        cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts à la cible
                    elif event.key == pygame.K_z:  # Sort de Soin
                        choix = 2
                        if self.nb_soin > 0:  # Vérifie si des sorts de soin sont disponibles
                            self.nb_soin -= 1  # Diminue le compteur de sorts de soin
                            self.soigner(20, fenetre)  # Soigne le Mage de 20 PV
                        else:
                            # Affiche un message indiquant que les sorts de soin sont épuisés
                            self.action = True
                            self.bandeau.afficher_message("Vous n'avez plus de soin", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message
                    elif event.key == pygame.K_e:  # Explosion Magique
                        choix = 3
                        if self.nb_explosion > 0:  # Vérifie si des sorts d'explosion sont disponibles
                            self.nb_explosion -= 1  # Diminue le compteur de sorts d'explosion
                            degats = 3 * self.attaque - cible.defense  # Calcule les dégâts infligés
                            cible.recevoir_attaque(degats, fenetre)  # Applique les dégâts à la cible
                        else:
                            # Affiche un message indiquant que les sorts d'explosion sont épuisés
                            self.action = True
                            self.bandeau.afficher_message("Vous n'avez plus d'explosion mage", fenetre)
                            pygame.time.wait(500)  # Pause pour afficher le message

    def carte_effet(self):
        """
        Applique les effets du terrain sur les attributs du Mage (ralentissement, esquive, etc.).
        """
        if (self.rect.x, self.rect.y) in self.boue:  # Si le Mage est sur une case de boue
            self.vitesse = 1  # Réduit la vitesse de déplacement
        elif (self.rect.x, self.rect.y) in self.arbre:  # Si le Mage est sur une case d'arbre
            self.esquive = 0.8  # Augmente la probabilité d'esquiver une attaque
        else:
            # Réinitialise les valeurs par défaut si aucune condition spéciale n'est remplie
            self.vitesse = mage_vitesse
            self.esquive = mage_esquive
