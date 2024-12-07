import pygame
import sys
import random
from chevalier import Chevalier
from archer import Archer
from mage import Mage
from grille import Grille
from bandeau_inferieur import BandeauInferieur
from carte import Carte
from constante import *

# Initialisation de Pygame
pygame.init()

class Game:
    def __init__(self):
        # Création de la fenêtre
        self.fenetre = pygame.display.set_mode(RESOLUTION_JEU)
        pygame.display.set_caption("Jeu de Tactique Tour par Tour")

        # Création de la grille
        taille_x = RESOLUTION[0] // TAILLE_CASE
        taille_y = RESOLUTION[1] // TAILLE_CASE
        self.grille = Grille(taille_x, taille_y, 0, 0)

        # Création de la carte
        self.carte = Carte("map2.tmx")  # Assurez-vous que "map2.tmx" est un fichier TMX valide

        # Initialisation du bandeau inférieur
        self.bandeau = BandeauInferieur()

        # Création des personnages
        self.archer = Archer(2 * TAILLE_CASE, 2 * TAILLE_CASE, "Empire Adrastien")
        self.mage = Mage(5 * TAILLE_CASE, 5 * TAILLE_CASE, "Empire Adrastien")
        self.chevalier = Chevalier(8 * TAILLE_CASE, 8 * TAILLE_CASE, "Empire Adrastien")

        # Liste des personnages
        self.liste_personnages = [self.archer, self.mage, self.chevalier]

        # Variables de jeu
        self.personnage_selectionne = None
        self.tour = 0
        self.jeu_en_cours = True

    def afficher(self):
        """Affiche la carte, la grille, les personnages et le bandeau."""
        self.fenetre.fill(BLANC)  # Fond blanc

        # Afficher la carte
        self.carte.afficher(self.fenetre)

        # Afficher la grille
        self.grille.afficher(self.fenetre)

        # Afficher les personnages
        for personnage in self.liste_personnages:
            personnage.afficher_personnage(self.fenetre)

            # Afficher les PV au-dessus du personnage
            font = pygame.font.SysFont(None, 24)
            pv_text = font.render(f"PV: {personnage.pv}", True, NOIR)
            self.fenetre.blit(pv_text, (personnage.rect.x + TAILLE_CASE // 4, personnage.rect.y - 20))

        # Afficher le bandeau inférieur
        self.bandeau.afficher(self.fenetre)
        if self.personnage_selectionne:
            self.bandeau.afficher_personnage(self.fenetre, self.personnage_selectionne.image_path,
                                             self.personnage_selectionne.pv, self.personnage_selectionne.attaque,
                                             self.personnage_selectionne.defense)
            self.bandeau.afficher_tour(self.fenetre, self.tour)

    def verifier_clic(self, event):
        """Gère les clics pour sélectionner un personnage."""
        mouse_pos = pygame.mouse.get_pos()
        for personnage in self.liste_personnages:
            if personnage.rect.collidepoint(mouse_pos):
                self.personnage_selectionne = personnage
                print(f"{personnage.__class__.__name__} sélectionné !")
                return

    def gerer_touches(self, event):
        """Gère les actions liées aux touches."""
        if event.key == pygame.K_RETURN:  # Fin du tour
            self.personnage_selectionne = None
            self.tour += 1
            print(f"Fin du tour {self.tour}. Tour du joueur suivant.")

        elif self.personnage_selectionne:
            # Compétences du personnage sélectionné
            cible = self.choisir_cible(self.personnage_selectionne)
            if cible:
                # Vérification de l'esquive de la cible
                if random.random() > cible.esquive:  # Si l'attaque n'est pas esquivée
                    if isinstance(self.personnage_selectionne, Archer):
                        print("1. Tir Précis  2. Tir Empoisonné  3. Pluie de Flèches  4. Tir Rapide")
                        choix = input("Choisissez une compétence : ")
                        if choix == "1":
                            degats = max(0, self.personnage_selectionne.attaque - cible.defense)
                            cible.recevoir_attaque(degats)
                            print(f"{self.personnage_selectionne.__class__.__name__} inflige {degats} dégâts avec Tir Précis.")
                        elif choix == "2":
                            degats = max(0, self.personnage_selectionne.attaque - cible.defense)
                            cible.recevoir_attaque(degats)
                            cible.etat = "empoisonné"
                            print(f"{cible.__class__.__name__} est maintenant empoisonné !")
                        elif choix == "3":
                            autres_cibles = [p for p in self.liste_personnages if p != self.personnage_selectionne]
                            for autre_cible in autres_cibles:
                                degats = max(5, self.personnage_selectionne.attaque // 2 - autre_cible.defense)
                                autre_cible.recevoir_attaque(degats)
                                print(f"{autre_cible.__class__.__name__} perd {degats} PV.")
                        elif choix == "4":
                            for _ in range(2):
                                degats = max(0, self.personnage_selectionne.attaque - cible.defense)
                                cible.recevoir_attaque(degats)
                                print(f"{self.personnage_selectionne.__class__.__name__} inflige {degats} dégâts avec Tir Rapide.")

                    elif isinstance(self.personnage_selectionne, Mage):
                        print("1. Boule de Feu  2. Soin  3. Explosion Magique  4. Téléportation")
                        choix = input("Choisissez une compétence : ")
                        if choix == "1":
                            degats = max(0, (self.personnage_selectionne.attaque * 2) - cible.defense)
                            cible.recevoir_attaque(degats)
                            print(f"{self.personnage_selectionne.__class__.__name__} inflige {degats} dégâts avec Boule de Feu.")
                        elif choix == "2":
                            self.personnage_selectionne.soigner(self.personnage_selectionne)
                            print(f"{self.personnage_selectionne.__class__.__name__} soigne {self.personnage_selectionne.__class__.__name__}.")
                        elif choix == "3":
                            autres_cibles = [p for p in self.liste_personnages if p != self.personnage_selectionne]
                            for autre_cible in autres_cibles:
                                degats = max(0, (self.personnage_selectionne.attaque * 1.5) - autre_cible.defense)
                                autre_cible.recevoir_attaque(degats)
                                print(f"{autre_cible.__class__.__name__} perd {degats} PV.")
                        elif choix == "4":
                            x, y = map(int, input("Entrez les nouvelles coordonnées x, y : ").split(","))
                            self.personnage_selectionne.teleportation(x, y)
                            print(f"{self.personnage_selectionne.__class__.__name__} se téléporte à ({x}, {y}).")

                    elif isinstance(self.personnage_selectionne, Chevalier):
                        print("1. Coup Puissant  2. Protection  3. Bouclier Divin  4. Frappe de Zone")
                        choix = input("Choisissez une compétence : ")
                        if choix == "1":
                            degats = max(0, (self.personnage_selectionne.attaque * 1.5) - cible.defense)
                            cible.recevoir_attaque(degats)
                            print(f"{self.personnage_selectionne.__class__.__name__} inflige {degats} dégâts avec Coup Puissant.")
                        elif choix == "2":
                            allies = [p for p in self.liste_personnages if p != self.personnage_selectionne]
                            self.personnage_selectionne.protection(allies)
                            print(f"{self.personnage_selectionne.__class__.__name__} utilise Protection.")
                        elif choix == "3":
                            self.personnage_selectionne.bouclier_divin()
                            print(f"{self.personnage_selectionne.__class__.__name__} utilise Bouclier Divin.")
                        elif choix == "4":
                            autres_cibles = [p for p in self.liste_personnages if p != self.personnage_selectionne]
                            for autre_cible in autres_cibles:
                                degats = max(10, self.personnage_selectionne.attaque - autre_cible.defense)
                                autre_cible.recevoir_attaque(degats)
                                print(f"{autre_cible.__class__.__name__} perd {degats} PV.")
                else:
                    print(f"{cible.__class__.__name__} esquive l'attaque !")

            # Déplacements avec les touches fléchées
            if event.key == pygame.K_UP:
                self.personnage_selectionne.rect.y -= TAILLE_CASE
            elif event.key == pygame.K_DOWN:
                self.personnage_selectionne.rect.y += TAILLE_CASE
            elif event.key == pygame.K_LEFT:
                self.personnage_selectionne.rect.x -= TAILLE_CASE
            elif event.key == pygame.K_RIGHT:
                self.personnage_selectionne.rect.x += TAILLE_CASE

    def choisir_cible(self, attacker):
        """Retourne une cible ennemie la plus proche de l'attaquant."""
        cibles = [p for p in self.liste_personnages if p != attacker and p.pv > 0]
        if not cibles:
            return None

        # Trouve la cible la plus proche
        cible_la_plus_proche = min(cibles, key=lambda cible: abs(attacker.rect.x - cible.rect.x) + abs(attacker.rect.y - cible.rect.y))
        return cible_la_plus_proche

    def verifier_fin_de_jeu(self):
        """Vérifie si le jeu est terminé."""
        survivants = [p for p in self.liste_personnages if p.pv > 0]
        if len(survivants) == 1:
            print(f"Le gagnant est {survivants[0].__class__.__name__}!")
            self.jeu_en_cours = False

    def boucle_principale(self):
        """Boucle principale du jeu."""
        while self.jeu_en_cours:
            self.afficher()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.verifier_clic(event)

                elif event.type == pygame.KEYDOWN:
                    self.gerer_touches(event)

            self.verifier_fin_de_jeu()

            pygame.display.flip()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    jeu = Game()
    jeu.boucle_principale()
"""
1. Démarrage et configuration
Lorsque le programme est lancé, Pygame est initialisé, et la fenêtre de jeu est créée.
La grille de jeu est configurée pour afficher le terrain, et la carte est chargée pour afficher l'environnement du jeu.
Les personnages (Archer, Mage, Chevalier) sont créés et placés sur la carte.
2. Affichage des éléments du jeu
La méthode afficher() est appelée à chaque boucle de jeu pour afficher :
La carte (en utilisant la classe Carte).
La grille (utilisant la classe Grille).
Les personnages (affichés à l'aide de leur méthode afficher_personnage()).
Un bandeau inférieur qui affiche des informations sur le personnage sélectionné (utilisant la classe BandeauInferieur).
3. Interaction avec les personnages
Sélection d'un personnage :
Lorsque le joueur clique sur un personnage avec la souris, la méthode verifier_clic() détecte le clic et sélectionne le personnage.
Le personnage sélectionné est mis en surbrillance, et ses détails apparaissent sur le bandeau inférieur.
Déplacement :
Le joueur peut déplacer le personnage sélectionné en utilisant les touches fléchées (K_UP, K_DOWN, K_LEFT, K_RIGHT). Le personnage se déplace d'une case dans la direction choisie.
Utilisation de compétences :
Lorsqu'un personnage est sélectionné, le joueur appuie sur la touche Espace pour accéder au menu des compétences disponibles.
Le joueur choisit une compétence en entrant un numéro, et la compétence est exécutée. Certaines compétences infligent des dégâts, tandis que d'autres ont des effets de soutien (comme le soin).
Les attaques prennent en compte l'attribut esquive de la cible. Si l'attaque est esquivée (basée sur une probabilité aléatoire), l'attaque est annulée, sinon elle inflige des dégâts.
4. Mécanismes de jeu
Compétences des personnages :
Chaque personnage a un ensemble de compétences spécifiques :
Archer : Tir Précis, Tir Empoisonné, Pluie de Flèches, Tir Rapide.
Mage : Boule de Feu, Soin, Explosion Magique, Téléportation.
Chevalier : Coup Puissant, Protection, Bouclier Divin, Frappe de Zone.
Les compétences ont des effets variés, allant de l'infligeant des dégâts à la guérison ou la protection des alliés.
Vérification de la fin de jeu :
Le jeu continue jusqu'à ce qu'un seul personnage reste en vie. La méthode verifier_fin_de_jeu() vérifie les PV des personnages et déclare un gagnant lorsque tous les autres sont éliminés.
5. Sélection de la cible
La méthode choisir_cible() sélectionne automatiquement la cible la plus proche de l'attaquant, en calculant la distance de Manhattan (somme des différences de coordonnées x et y) entre le personnage sélectionné et les autres personnages en vie.
6. Esquive
Lorsqu'une attaque est effectuée, la probabilité d'esquive de la cible est prise en compte. Si un tir est esquivé (random.random() > cible.esquive), l'attaque échoue, et le message "esquive l'attaque" est affiché. Sinon, les dégâts sont appliqués à la cible.
7. Affichage de la progression
Les informations sur les PV des personnages sont affichées au-dessus de chaque personnage.
Le bandeau inférieur affiche des détails sur le personnage sélectionné, et il est mis à jour à chaque tour.
"""