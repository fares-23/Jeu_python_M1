from archer import Archer
from mage import Mage
from chevalier import Chevalier
from grille import Grille
from constante import *
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
fenetre = pygame.display.set_mode((TAILLE_GRILLE * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE))

# Création de la grille, du personnage et des personnages ennemis
grille = Grille(TAILLE_GRILLE, fenetre)

arche = Archer(3 * TAILLE_CASE, 3 * TAILLE_CASE, (150, 0, 0))  # L'archer est rouge
mage = Mage(7 * TAILLE_CASE, 7 * TAILLE_CASE, (0, 150, 0))  # Le mage est vert
chevalier = Chevalier(5 * TAILLE_CASE, 5 * TAILLE_CASE, (0, 0, 150))  # Le chevalier est bleu

# Liste des personnages
liste_personnage = [arche, mage, chevalier]

# Fonction pour choisir une cible pour un personnage
def choisir_cible(attacker, personnages):
    """Choisit une cible valide pour un personnage."""
    cibles = [p for p in personnages if p != attacker and p.pv > 0]
    if cibles:
        return cibles[0]  # Retourne la première cible valide
    return None

while True:
    # Coordonnées actuelles des personnages
    coordonnee = [arche.get_coordonnees(), mage.get_coordonnees(), chevalier.get_coordonnees()]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche : déplacement
                for personnage in liste_personnage:
                    personnage.deplacement(grille, event, coordonnee)

            elif event.button == 3:  # Clic droit : compétences
                for personnage in liste_personnage:
                    if isinstance(personnage, Archer):
                        # L'Archer choisit entre Tir Rapide et Pluie de Flèches
                        cible = choisir_cible(personnage, liste_personnage)
                        autres_cibles = [p for p in liste_personnage if p != cible and p != personnage]
                        if cible:
                            print("Choix pour Archer : 1. Tir Rapide 2. Tir Empoisonné 3. Pluie de Flèches")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                personnage.tir_rapide(cible)
                            elif choix == "2":
                                personnage.tir_empoisonne(cible)
                            elif choix == "3":
                                personnage.pluie_de_fleches(autres_cibles)

                    elif isinstance(personnage, Mage):
                        # Le Mage choisit entre Explosion Magique, Soin, ou Téléportation
                        cible = choisir_cible(personnage, liste_personnage)
                        if cible:
                            print("Choix pour Mage : 1. Boule de Feu 2. Soin 3. Explosion Magique 4. Téléportation")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                personnage.utiliser_competence(cible)
                            elif choix == "2":
                                personnage.soigner(personnage)  # Soigne lui-même ou un allié
                            elif choix == "3":
                                personnage.explosion_magique(liste_personnage)
                            elif choix == "4":
                                x, y = map(int, input("Entrez les nouvelles coordonnées x, y : ").split(","))
                                personnage.teleportation(x, y)

                    elif isinstance(personnage, Chevalier):
                        # Le Chevalier choisit entre Coup Puissant, Protection, Bouclier Divin ou Frappe de Zone
                        cible = choisir_cible(personnage, liste_personnage)
                        autres_cibles = [p for p in liste_personnage if p != personnage]
                        if cible:
                            print("Choix pour Chevalier : 1. Coup Puissant 2. Protection 3. Bouclier Divin 4. Frappe de Zone")
                            choix = input("Choisissez une compétence : ")
                            if choix == "1":
                                personnage.utiliser_competence(cible)
                            elif choix == "2":
                                personnage.protection(liste_personnage)
                            elif choix == "3":
                                personnage.bouclier_divin()
                            elif choix == "4":
                                personnage.frappe_de_zone(autres_cibles)

    # Affichage de la grille et des personnages
    fenetre.fill((255, 255, 255))  # Efface l'écran
    grille.afficher()

    for personnage in liste_personnage:
        # Affichage des déplacements possibles et du personnage
        personnage.afficher_deplacement(grille.cases, fenetre, coordonnee)
        personnage.afficher_personnage(fenetre)

        # Affichage des PV au-dessus de chaque personnage
        font = pygame.font.SysFont(None, 24)
        pv_text = font.render(f"PV: {personnage.pv}", True, (0, 0, 0))
        fenetre.blit(pv_text, (personnage.x, personnage.y - 20))

    pygame.display.update()  # Met à jour l'affichage
