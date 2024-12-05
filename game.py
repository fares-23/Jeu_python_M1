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
"""