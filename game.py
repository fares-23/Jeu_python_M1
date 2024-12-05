import pygame
from archer import Archer
from chevalier import Chevalier
from mage import Mage
from grille import Grille
from constante import *
import sys

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
fenetre = pygame.display.set_mode(RESOLUTION)

# Création de la grille
grille = Grille(TAILLE_GRILLE, fenetre)

# Création des personnages
archer = Archer(2 * TAILLE_CASE, 2 * TAILLE_CASE, (255, 0, 0))  # Rouge
mage = Mage(5 * TAILLE_CASE, 5 * TAILLE_CASE, (0, 255, 0))  # Vert
chevalier = Chevalier(8 * TAILLE_CASE, 8 * TAILLE_CASE, (0, 0, 255))  # Bleu

# Liste des personnages
liste_personnage = [archer, mage, chevalier]

# Variable pour garder le personnage sélectionné
personnage_selectionne = None  # Aucun personnage sélectionné par défaut

# Fonction pour gérer le choix d'une cible
def choisir_cible(attacker, personnages):
    """Retourne une cible valide pour l'attaquant."""
    cibles = [p for p in personnages if p != attacker and p.pv > 0]
    if cibles:
        return cibles[0]  # Retourne la première cible valide
    return None

# Boucle principale
while True:
    fenetre.fill((255, 255, 255))  # Fond blanc

    # Affichage de la grille
    grille.afficher()

    # Affichage des personnages
    for personnage in liste_personnage:
        personnage.afficher_personnage(fenetre)

        # Affichage des PV au-dessus du personnage
        font = pygame.font.SysFont(None, 24)
        pv_text = font.render(f"PV: {personnage.pv}", True, (0, 0, 0))
        fenetre.blit(pv_text, (personnage.rect.x, personnage.rect.y - 20))

    pygame.display.update()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Détection d'un clic gauche pour sélectionner un personnage
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            mouse_pos = pygame.mouse.get_pos()
            for personnage in liste_personnage:
                if personnage.rect.collidepoint(mouse_pos):  # Vérifie si le clic est sur un personnage
                    personnage_selectionne = personnage  # Change le personnage sélectionné
                    print(f"{personnage.__class__.__name__} sélectionné !")

        # Si un personnage est sélectionné, gestion des actions
        if personnage_selectionne:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Fin du tour
                    personnage_selectionne = None  # Désélectionne le personnage
                    print("Fin du tour. Aucun personnage sélectionné.")

                elif event.key == pygame.K_SPACE:  # Activer une compétence
                    cible = choisir_cible(personnage_selectionne, liste_personnage)
                    if cible:
                        if isinstance(personnage_selectionne, Archer):
                            print("1. Tir Précis  2. Tir Empoisonné  3. Pluie de Flèches  4. Tir Rapide")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                degats = personnage_selectionne.attaque - cible.defense
                                cible.recevoir_attaque(degats)
                            elif choix == "2":
                                degats = personnage_selectionne.attaque - cible.defense
                                cible.recevoir_attaque(degats)
                                cible.etat = "empoisonné"
                                print(f"{cible.__class__.__name__} est maintenant empoisonné !")
                            elif choix == "3":
                                autres_cibles = [p for p in liste_personnage if p != personnage_selectionne]
                                for autre_cible in autres_cibles:
                                    degats = max(5, personnage_selectionne.attaque // 2 - autre_cible.defense)
                                    autre_cible.recevoir_attaque(degats)
                            elif choix == "4":
                                for _ in range(2):  # Deux attaques rapides
                                    degats = personnage_selectionne.attaque - cible.defense
                                    cible.recevoir_attaque(degats)

                        elif isinstance(personnage_selectionne, Mage):
                            print("1. Boule de Feu  2. Soin  3. Explosion Magique  4. Téléportation")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                degats = personnage_selectionne.attaque * 2 - cible.defense
                                cible.recevoir_attaque(degats)
                            elif choix == "2":
                                personnage_selectionne.soigner(personnage_selectionne)
                            elif choix == "3":
                                for autre_cible in liste_personnage:
                                    degats = personnage_selectionne.attaque * 1.5 - autre_cible.defense
                                    autre_cible.recevoir_attaque(degats)
                            elif choix == "4":
                                x, y = map(int, input("Entrez les nouvelles coordonnées x, y : ").split(","))
                                personnage_selectionne.teleportation(x, y)

                        elif isinstance(personnage_selectionne, Chevalier):
                            print("1. Coup Puissant  2. Protection  3. Bouclier Divin  4. Frappe de Zone")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                degats = personnage_selectionne.attaque * 1.5 - cible.defense
                                cible.recevoir_attaque(degats)
                            elif choix == "2":
                                for autre_personnage in liste_personnage:
                                    autre_personnage.defense += 5
                                    print(f"La défense de {autre_personnage.__class__.__name__} augmente temporairement.")
                            elif choix == "3":
                                print(f"{personnage_selectionne.__class__.__name__} devient invincible pour ce tour !")
                            elif choix == "4":
                                autres_cibles = [p for p in liste_personnage if p != personnage_selectionne]
                                for autre_cible in autres_cibles:
                                    degats = max(10, personnage_selectionne.attaque - autre_cible.defense)
                                    autre_cible.recevoir_attaque(degats)

                # Déplacement via le clavier
                elif event.key == pygame.K_UP:  # Vers le haut
                    personnage_selectionne.rect.y -= TAILLE_CASE
                elif event.key == pygame.K_DOWN:  # Vers le bas
                    personnage_selectionne.rect.y += TAILLE_CASE
                elif event.key == pygame.K_LEFT:  # À gauche
                    personnage_selectionne.rect.x -= TAILLE_CASE
                elif event.key == pygame.K_RIGHT:  # À droite
                    personnage_selectionne.rect.x += TAILLE_CASE

    # Vérification des PV et fin de partie
    liste_personnage = [p for p in liste_personnage if p.pv > 0]
    if len(liste_personnage) == 1:
        print(f"Le gagnant est {liste_personnage[0].__class__.__name__}!")
        pygame.quit()
        sys.exit()
<<<<<<< HEAD
""" 
1. Lancement du jeu
Initialisation :

Le jeu se lance avec une fenêtre affichant une grille de cases et les personnages placés à des positions fixes.
Chaque personnage a des statistiques spécifiques (PV, défense, vitesse, etc.) et des compétences uniques.
Objectif :

Rester le dernier personnage vivant en utilisant des attaques, des compétences, et des stratégies de déplacement.
2. Sélection d’un personnage
Cliquez sur un personnage avec le bouton gauche de la souris pour le sélectionner.
Une fois sélectionné :
Vous pouvez le déplacer sur la grille.
Vous pouvez utiliser ses compétences pour attaquer ou se protéger.
3. Déplacement
Touches directionnelles (↑, ↓, ←, →) :
Ces touches permettent de déplacer le personnage actif d'une case dans la direction choisie.
Chaque personnage a une vitesse qui détermine combien de cases il peut se déplacer en un tour.
4. Utilisation des compétences
Appuyez sur SPACE :
Les compétences disponibles pour le personnage sélectionné s'affichent dans la console.
Entrez le numéro correspondant à la compétence que vous voulez utiliser (ex. : 1 pour la première compétence).
Les compétences peuvent :
Attaquer un adversaire.
Affecter plusieurs adversaires en zone.
Soigner des alliés ou le personnage lui-même.
Appliquer des effets spéciaux comme l’empoisonnement ou l’invincibilité.
5. Attaque et Esquive
Lorsqu’une attaque est effectuée :
Calcul des dégâts :
Les dégâts sont basés sur les statistiques d'attaque et de défense du personnage.
Esquive :
Avant d'infliger les dégâts, la cible a une chance d'esquiver l'attaque.
Si l’esquive réussit, aucun dégât n’est infligé :
python
if random.random() < cible.esquive:
    print(f"{cible.__class__.__name__} esquive l'attaque !")
Si l’esquive échoue, les PV sont réduits.
6. Fin du tour
Appuyez sur RETURN pour terminer le tour.
Cela permet de désélectionner le personnage actif et de passer à une nouvelle action.
7. Vérification des PV
Après chaque tour :
Les personnages ayant 0 PV ou moins sont éliminés.
S’il ne reste qu’un personnage vivant, il est déclaré gagnant :
python
if len(liste_personnage) == 1:
    print(f"Le gagnant est {liste_personnage[0].__class__.__name__}!")
8. Compétences des personnages
Archer (Rouge) :
Tir Précis : Inflige des dégâts directs à une cible unique.
Tir Empoisonné : Inflige des dégâts et empoisonne la cible.
Pluie de Flèches : Attaque tous les adversaires dans une zone.
Tir Rapide : Tire deux fois rapidement sur une cible.
Mage (Vert) :
Boule de Feu : Inflige des dégâts massifs à une cible.
Soin : Restaure des PV à lui-même ou à un allié.
Explosion Magique : Attaque tous les ennemis à la fois.
Téléportation : Déplace instantanément le Mage à une position de la grille.
Chevalier (Bleu) :
Coup Puissant : Inflige de gros dégâts à une cible unique.
Protection : Augmente temporairement la défense des alliés.
Bouclier Divin : Rend le Chevalier invincible pour un tour.
Frappe de Zone : Attaque tous les ennemis autour de lui.
=======

"""
Pygame démarre :

La bibliothèque Pygame initialise l'interface graphique.
Une fenêtre est créée pour afficher la grille et les personnages.
Création de la grille et des personnages :

La grille représente le terrain de jeu, divisé en cases.
Trois personnages (Archer, Mage, Chevalier) sont placés sur la grille à des positions prédéfinies. Chaque personnage a :
Une couleur pour le distinguer.
Des points de vie (PV).
Des compétences uniques.
Variables de gestion :

Une liste liste_personnage contient les trois personnages.
Une variable personnage_selectionne est utilisée pour garder une référence au personnage actuellement sélectionné.
2. Affichage
À chaque tour, la fenêtre est mise à jour :
Grille : La grille est affichée en arrière-plan.
Personnages : Les personnages sont affichés sur leurs positions actuelles.
Points de vie : Les PV de chaque personnage sont affichés au-dessus de lui.
3. Sélection des Personnages
Clic gauche : Lorsque l'utilisateur clique sur un personnage, ce personnage devient le personnage actif (sélectionné).
Cela est détecté avec la fonction collidepoint, qui vérifie si le clic de la souris se trouve sur le personnage.
La sélection est indiquée dans la console par un message comme Archer sélectionné !.
4. Actions du Personnage Sélectionné
Une fois un personnage sélectionné, l'utilisateur peut effectuer différentes actions :

a. Déplacement
Utilisez les flèches directionnelles pour déplacer le personnage sur la grille :
UP : Déplace vers le haut.
DOWN : Déplace vers le bas.
LEFT : Déplace à gauche.
RIGHT : Déplace à droite.
La position est mise à jour en ajustant les coordonnées du rectangle rect du personnage.
b. Compétences
Appuyez sur SPACE pour activer une compétence :
Le programme demande à l'utilisateur de choisir une compétence via la console.
Une cible est automatiquement sélectionnée (le premier ennemi valide avec des PV > 0).
En fonction de la compétence choisie, le personnage effectue une action, comme :
Infliger des dégâts à une cible.
Soigner un allié.
Effectuer une attaque de zone.
Se téléporter.
c. Fin du Tour
Appuyez sur RETURN pour terminer le tour.
Le personnage sélectionné est désélectionné.
Le joueur peut cliquer sur un autre personnage pour commencer un nouveau tour.
5. Gestion des PV et Fin de Partie
Mise à jour des PV :

Les personnages qui ont 0 PV ou moins sont retirés de liste_personnage.
Leurs points de vie sont affichés en temps réel au-dessus d'eux.
Fin du jeu :

Lorsque la liste liste_personnage ne contient qu’un seul personnage, le jeu se termine.
Le personnage restant est déclaré vainqueur, et le programme affiche son type (ex. : Le gagnant est Archer !).
"""

""" 
. Lancement du Jeu
Initialisation : Lorsque vous exécutez le programme (python jeu.py), Pygame s'initialise et une fenêtre de jeu s'ouvre, affichant la grille sur laquelle les personnages se déplacent.
Affichage de la grille : La grille est dessinée sur l'écran, servant de terrain de jeu pour les personnages.
2. Présentation des Personnages
Trois types de personnages sont disponibles :
Archer : Un personnage avec des attaques à distance et des compétences comme le "Tir Précis" et la "Pluie de Flèches".
Mage : Un personnage qui utilise des compétences magiques telles que la "Boule de Feu" et le "Soin".
Chevalier : Un personnage de mêlée qui peut utiliser des compétences de protection et de zone, comme le "Coup Puissant" et la "Frappe de Zone".
Chaque personnage a une couleur différente pour le distinguer facilement :
Archer : Rouge
Mage : Vert
Chevalier : Bleu
3. Tour de Jeu
Gestion des tours : Le jeu est structuré en tours. Un joueur actif prend son tour pour déplacer son personnage, choisir une cible et utiliser des compétences.
Changement de tour : Lorsque le joueur appuie sur RETURN, le programme passe au joueur suivant en mettant à jour la variable joueur_actuel, qui pointe vers le prochain personnage de la liste.
4. Interaction avec les Personnages
Déplacement :

Utilisez les touches directionnelles (UP, DOWN, LEFT, RIGHT) pour déplacer le personnage actif sur la grille.
Un clic gauche de la souris est également utilisé pour déplacer le personnage vers une case cliquée, en appelant la méthode grille.deplacer_personnage().
Utilisation des compétences :

Lorsqu'une touche SPACE est pressée, le programme affiche les compétences disponibles pour le personnage actif dans la console.
L'utilisateur choisit une compétence en entrant un numéro (ex. : "1" pour "Tir Précis") et appuie sur ENTER.
Le programme exécute la compétence choisie sur une cible. Si une compétence nécessite des coordonnées (comme la téléportation du Mage), l'utilisateur doit entrer ces coordonnées via input.
5. Sélection de la Cible
Cible automatique : La fonction choisir_cible() sélectionne automatiquement la première cible valide (un autre personnage ayant encore des PV).
Clic pour sélectionner la cible : Si le programme est configuré pour permettre la sélection par clic, le joueur peut cliquer sur un personnage pour le sélectionner comme cible.
Affichage des options de compétence : Après la sélection de la cible, l'utilisateur choisit la compétence à utiliser, ce qui déclenche l'effet de la compétence.
6. Affichage des Points de Vie (PV)
Affichage des PV : Les points de vie de chaque personnage sont affichés au-dessus de leur position sur la grille. Cela permet de suivre l'état de santé de chaque personnage.
7. Exécution des Compétences
Compétences des personnages :
Les compétences des personnages sont définies dans les classes Archer, Mage, et Chevalier. Par exemple, l'Archer peut utiliser le "Tir Précis" pour infliger des dégâts directs, tandis que le Mage peut utiliser la "Boule de Feu" pour attaquer à distance.
Effets des compétences : Selon la compétence choisie, des effets différents sont appliqués, comme réduire les PV d'une cible, soigner un allié ou changer de position sur la grille (téléportation).
8. Fin de Partie
Vérification des PV : À chaque tour, le programme vérifie si des personnages ont des PV <= 0 et les élimine de la liste des personnages.
Déclaration du gagnant : Le jeu se termine lorsqu'il ne reste plus qu'un seul personnage en vie, qui est déclaré vainqueur.
>>>>>>> a786aef655e57c984f0b9be2482b4154fd521442
"""