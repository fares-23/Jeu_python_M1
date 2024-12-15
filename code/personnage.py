import pygame
from constante import *
import sys
from bandeau_inferieur import BandeauInferieur
from abc import ABC, abstractmethod
import random
from carte import Carte

# La classe Personnage est une classe abstraite qui définit un personnage dans le jeu.
# Elle contient les attributs et méthodes de base nécessaires pour gérer un personnage (attaque, défense, vie, déplacement, etc.).
class Personnage(ABC):
    
    # Le constructeur initialise les attributs de base du personnage.
    def __init__(self, x, y, image_path):
        # Attributs de base du personnage (nom, attaque, défense, points de vie, vitesse, esquive, royaume, etc.)
        self.nom = None
        self.attaque = None
        self.defense = None
        self.pv = None
        self.vitesse = None
        self.esquive = None
        self.royaume = None
        
        self.action = None  # True si le personnage n'a pas encore joué, False sinon
        
        # Définition d'un rectangle représentant le personnage à une position (x, y) avec la taille de la case (TAILLE_CASE)
        self.rect = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
        
        # Attributs pour gérer la sélection du personnage et les déplacements possibles
        self.selectionne = False
        self.afficher_deplacement_possible = False
        
        # Le chemin vers l'image du personnage (affichage graphique)
        self.image_path = None
        
        # Bandeau pour afficher des informations comme les points de vie, attaque, défense, etc.
        self.bandeau = BandeauInferieur()
        
        # Zones pour gérer les déplacements et attaques possibles
        self.zone = []
        self.zone_attaque = []
        self.coordonnee = None
        self.boue = []  # Zones spéciales comme la boue
        self.arbre = []  # Zones spéciales comme les arbres
        self.carte = []  # Carte du jeu
        
    # La méthode afficher_deplacement permet de gérer l'affichage des cases où le personnage peut se déplacer.
    def afficher_deplacement(self, grille, fenetre, coordonnee, carte):
        # Met à jour les zones de la carte que le personnage peut atteindre
        self.carte = carte
        self.coordonnee = coordonnee
        self.arbre = [] + carte.recuperer_coordonnees_calque("arbre")  # Récupère les coordonnées des arbres
        self.boue = [] + carte.recuperer_coordonnees_calque("boue")    # Récupère les coordonnées de la boue
        
        # Si l'affichage des déplacements est activé, on commence à afficher les cases possibles
        if self.afficher_deplacement_possible:
            # Récupération des coordonnées des obstacles
            obstacles = (
                carte.recuperer_coordonnees_calque("maison")
                + carte.recuperer_coordonnees_calque("eau")
                + carte.recuperer_coordonnees_calque("rocher")
            )
            
            # Parcourt chaque case de la grille
            for ligne in grille:
                for case in ligne:
                    # Calcul de la distance entre le personnage et la case
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE

                    # Ignore les cases hors de portée ou déjà occupées
                    if abs(dx) + abs(dy) > self.vitesse or (case.x, case.y) in coordonnee:
                        continue

                    # Vérifie si un obstacle bloque la case
                    is_blocked = False
                    for obstacle in obstacles:
                        if dx > 0 and case.y == obstacle[1] and obstacle[0] <= case.x <= obstacle[0] + (dx - 1) * TAILLE_CASE:
                            is_blocked = True
                            break
                        if dx < 0 and case.y == obstacle[1] and obstacle[0] >= case.x >= obstacle[0] + (dx + 1) * TAILLE_CASE:
                            is_blocked = True
                            break
                        if dy > 0 and case.x == obstacle[0] and obstacle[1] <= case.y <= obstacle[1] + (dy - 1) * TAILLE_CASE:
                            is_blocked = True
                            break
                        if dy < 0 and case.x == obstacle[0] and obstacle[1] >= case.y >= obstacle[1] + (dy + 1) * TAILLE_CASE:
                            is_blocked = True
                            break

                    # Si la case n'est pas bloquée, on l'ajoute à la zone de déplacement
                    if not is_blocked:
                        pygame.draw.rect(fenetre, (16, 16, 205), case, 1)  # Affiche la case en bleu clair
                        self.bandeau.afficher_personnage(fenetre, self.image_path, self.pv, self.attaque, self.defense, self.esquive, self.royaume)
                        self.zone.append((case.x, case.y))
            
    # La méthode deplacement permet au personnage de se déplacer en fonction des clics de la souris.
    def deplacement(self, grille, event, coordonnee, carte):
        if self.action:  # Si le personnage n'a pas encore agi durant son tour
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    # Activer ou désactiver la sélection du personnage
                    self.selectionne = not self.selectionne
                    self.afficher_deplacement_possible = self.selectionne
                else:
                    # Vérifie si une case a été cliquée pour déplacer le personnage
                    for ligne in grille.cases:
                        for case in ligne:
                            if case.collidepoint(mouse_pos) and self.selectionne:
                                dx = (case.x - self.rect.x) // TAILLE_CASE
                                dy = (case.y - self.rect.y) // TAILLE_CASE

                                # Ignore les cases hors de portée ou déjà occupées
                                if abs(dx) + abs(dy) > self.vitesse or (case.x, case.y) in coordonnee:
                                    self.selectionne = not self.selectionne
                                    self.afficher_deplacement_possible = self.selectionne
                                    continue

                                # Vérifie si un obstacle bloque la case
                                obstacles = (
                                    carte.recuperer_coordonnees_calque("maison")
                                    + carte.recuperer_coordonnees_calque("eau")
                                    + carte.recuperer_coordonnees_calque("rocher")
                                )
                                is_blocked = False
                                for obstacle in obstacles:
                                    if dx > 0 and case.y == obstacle[1] and obstacle[0] <= case.x <= obstacle[0] + (dx - 1) * TAILLE_CASE:
                                        is_blocked = True
                                        break
                                    if dx < 0 and case.y == obstacle[1] and obstacle[0] >= case.x >= obstacle[0] + (dx + 1) * TAILLE_CASE:
                                        is_blocked = True
                                        break
                                    if dy > 0 and case.x == obstacle[0] and obstacle[1] <= case.y <= obstacle[1] + (dy - 1) * TAILLE_CASE:
                                        is_blocked = True
                                        break
                                    if dy < 0 and case.x == obstacle[0] and obstacle[1] >= case.y >= obstacle[1] + (dy + 1) * TAILLE_CASE:
                                        is_blocked = True
                                        break

                                # Si la case n'est pas bloquée, on déplace le personnage
                                if not is_blocked:
                                    self.rect.x = case.x
                                    self.rect.y = case.y
                                    self.afficher_deplacement_possible = False
                                    self.selectionne = False
                                    self.action = False
                                    return

    # La méthode afficher_personnage permet d'afficher l'image du personnage à sa position sur l'écran.
    def afficher_personnage(self, fenetre, liste_royaume=None):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (TAILLE_CASE, TAILLE_CASE))
        
        # Si le personnage appartient au premier royaume, l'image est retournée horizontalement
        if self.royaume == liste_royaume[0]:
            image = pygame.transform.flip(image, True, False)
        
        # Affiche l'image du personnage sur la fenêtre à la position de son rectangle
        fenetre.blit(image, self.rect)
    
    # La méthode get_coordonnees retourne les coordonnées du personnage (position x, y).
    def get_coordonnees(self):
        return (self.rect.x, self.rect.y)

    # La méthode zone_combat affiche les cases où le personnage peut attaquer.
    def zone_combat(self, fenetre, grille):
        # Si le personnage est un archer ou un mage, il peut attaquer à distance
        if self.nom == "archer" or self.nom == "mage":
            for ligne in grille:
                for case in ligne:
                    dx = (case.x - self.rect.x) // TAILLE_CASE
                    dy = (case.y - self.rect.y) // TAILLE_CASE
                    if (case.x, case.y) in self.coordonnee:
                        pass
                    elif abs(dx) + abs(dy) <= self.vitesse:
                        pygame.draw.rect(fenetre, ROUGE, case, 1)
                        self.bandeau.afficher_personnage(fenetre, self.image_path, self.pv, self.attaque, self.defense, self.esquive, self.royaume)
                        self.zone_attaque.append((case.x, case.y))
        else:
            # Zone d'attaque au corps à corps
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x = self.rect.x // TAILLE_CASE + dx
                    y = self.rect.y // TAILLE_CASE + dy
                    if 0 <= x < len(grille[0]) and 0 <= y < len(grille):
                        case = grille[y][x]
                        pygame.draw.rect(fenetre, ROUGE, case, 1)
                        self.zone_attaque.append((case.x, case.y))

    # La méthode competence est abstraite et doit être implémentée dans les sous-classes de Personnage.
    @abstractmethod
    def competence(self, cible, fenetre):
        pass
      
    # La méthode recevoir_attaque gère la prise de dégâts par le personnage, en tenant compte de l'esquive.
    def recevoir_attaque(self, degats, fenetre):
        if random.random() < self.esquive:
            self.bandeau.afficher_message(f"{self.nom} esquive l'attaque !", fenetre)
            pygame.display.flip()
            pygame.time.wait(500)
        else:
            if random.random() <= 0.2:
                degats = 2 * degats
                self.bandeau.afficher_message(f"{self.nom} subit un coup critique et reçoit {degats} dégâts !", fenetre)
            else:
                self.bandeau.afficher_message(f"{self.nom} reçoit {degats} dégâts !", fenetre)
            self.pv -= max(degats, 0)  # Empêche les PV d'être négatifs
            pygame.display.flip()
            pygame.time.wait(500)
        
    # La méthode soigner permet de régénérer des points de vie au personnage.
    def soigner(self, soin, fenetre):
        self.pv += soin
        self.bandeau.afficher_message(f"{self.nom} récupère {soin} PV !", fenetre)
        pygame.time.wait(500)

    # La méthode buff améliore la défense du personnage.
    def buff(self, buff, fenetre):
        self.defense += buff
        self.bandeau.afficher_message(f"{self.nom} gagne {buff} points de défense !", fenetre)
        pygame.time.wait(500)

    # La méthode carte_effet est abstraite et doit être implémentée dans les sous-classes pour appliquer les effets du terrain.
    @abstractmethod
    def carte_effet(self):
        pass
