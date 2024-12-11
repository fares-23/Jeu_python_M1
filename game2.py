#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:40:56 2024

@author: mamadoutandia
"""

import pygame
import sys
from chevalier import Chevalier
from archer import Archer
from mage import Mage
from grille import Grille
from bandeau_inferieur import BandeauInferieur
from carte import Carte
from constante import *

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
fenetre = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Jeu de Tactique")

# Création des composants principaux
grille = Grille(15, 15, 0, 0)  # Grille de 15x15 cases
carte = Carte("map2.tmx")
bandeau = BandeauInferieur()

# Création des personnages
chevalier = Chevalier(2 * TAILLE_CASE, 2 * TAILLE_CASE, royaume="Saint Royaume de Faerghus")
archer = Archer(5 * TAILLE_CASE, 5 * TAILLE_CASE, royaume="Alliance de Leicester")
mage = Mage(8 * TAILLE_CASE, 8 * TAILLE_CASE, royaume="Empire Adrastien")

# Liste des personnages
personnages = [chevalier, archer, mage]

# Variables de gestion
personnage_selectionne = None  # Le personnage actuellement sélectionné
running = True
clock = pygame.time.Clock()

# Définition des compétences
def utiliser_competence(personnage, cibles):
    """Gère l'utilisation des compétences en fonction du type du personnage."""
    if isinstance(personnage, Chevalier):
        print("1. Coup Puissant  2. Protection  3. Bouclier Divin  4. Frappe de Zone")
        choix = input("Choisissez une compétence : ")
        if choix == "1":
            personnage.coup_puissant(cibles[0])
        elif choix == "2":
            personnage.protection(personnages)
        elif choix == "3":
            personnage.bouclier_divin()
        elif choix == "4":
            personnage.frappe_de_zone(cibles)

    elif isinstance(personnage, Archer):
        print("1. Tir Précis  2. Pluie de Flèches  3. Tir Empoisonné  4. Tir Rapide")
        choix = input("Choisissez une compétence : ")
        if choix == "1":
            personnage.tir_precis(cibles[0])
        elif choix == "2":
            personnage.pluie_de_fleches(cibles)
        elif choix == "3":
            personnage.tir_empoisonne(cibles[0])
        elif choix == "4":
            personnage.tir_rapide(cibles[0])

    elif isinstance(personnage, Mage):
        print("1. Boule de Feu  2. Soin  3. Explosion Magique  4. Téléportation")
        choix = input("Choisissez une compétence : ")
        if choix == "1":
            personnage.boule_de_feu(cibles[0])
        elif choix == "2":
            personnage.soigner(personnage)
        elif choix == "3":
            personnage.explosion_magique(cibles)
        elif choix == "4":
            x, y = map(int, input("Entrez les coordonnées de téléportation (x, y) : ").split(","))
            personnage.teleportation(x * TAILLE_CASE, y * TAILLE_CASE)

# Gestion des événements
def gerer_clic_souris(event):
    """Gère la sélection d'un personnage par clic de souris."""
    global personnage_selectionne
    for personnage in personnages:
        if personnage.rect.collidepoint(event.pos):
            personnage_selectionne = personnage
            print(f"{personnage.__class__.__name__} sélectionné !")
            return

def gerer_clavier(event):
    """Gère les actions et déplacements au clavier."""
    global personnage_selectionne
    if personnage_selectionne:
        if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            dx, dy = 0, 0
            if event.key == pygame.K_UP:
                dy = -TAILLE_CASE
            elif event.key == pygame.K_DOWN:
                dy = TAILLE_CASE
            elif event.key == pygame.K_LEFT:
                dx = -TAILLE_CASE
            elif event.key == pygame.K_RIGHT:
                dx = TAILLE_CASE
            personnage_selectionne.rect.move_ip(dx, dy)

        elif event.key == pygame.K_RETURN:  # Fin de sélection
            personnage_selectionne = None
            print("Personnage désélectionné.")

        elif event.key == pygame.K_SPACE:  # Utilisation d'une compétence
            # Détermine les cibles potentielles (ennemis)
            cibles = [p for p in personnages if p != personnage_selectionne and p.pv > 0]
            if cibles:
                utiliser_competence(personnage_selectionne, cibles)

# Boucle principale
while running:
    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            gerer_clic_souris(event)
        elif event.type == pygame.KEYDOWN:
            gerer_clavier(event)

    # Mise à jour de l'écran
    fenetre.fill(BLANC)  # Fond blanc
    carte.afficher(fenetre)  # Affiche la carte TMX
    grille.afficher(fenetre, carte.tmx_data)  # Affiche la grille

    # Affiche les personnages
    for personnage in personnages:
        personnage.afficher_personnage(fenetre)

    # Bandeau d'informations
    bandeau.afficher(fenetre)
    if personnage_selectionne:
        bandeau.afficher_personnage(fenetre, personnage_selectionne.image_path,
                                    personnage_selectionne.pv, personnage_selectionne.attaque,
                                    personnage_selectionne.defense)

    # Vérifie les PV et fin de partie
    personnages = [p for p in personnages if p.pv > 0]  # Supprime les personnages morts
    if len(personnages) == 1:
        print(f"Le gagnant est {personnages[0].__class__.__name__} !")
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
"""
1. Initialisation
Le programme commence par l'initialisation de la bibliothèque Pygame et des composants nécessaires :

Fenêtre de jeu : La fenêtre de dimensions définies par RESOLUTION est créée pour afficher les éléments visuels du jeu.
Carte et grille :
La classe Carte charge une carte au format TMX (conçue avec un éditeur comme Tiled).
La classe Grille gère la disposition des cases et leur affichage pour représenter le terrain.
Personnages :
Trois personnages (Chevalier, Archer, Mage) sont créés avec des positions de départ spécifiques sur la grille.
Ils sont stockés dans une liste personnages.
2. Boucle principale
La boucle principale gère le fonctionnement continu du jeu :

Écoute des événements : La boucle surveille les actions du joueur (clavier et souris).
Mise à jour de l'affichage :
La carte, la grille et les personnages sont dessinés dans la fenêtre.
Si un personnage est sélectionné, ses informations (PV, attaque, défense) s’affichent dans le bandeau inférieur.
Fin de partie : Si un seul personnage reste en vie, la boucle se termine, et le programme affiche le gagnant.
3. Interactions utilisateur
Le joueur peut interagir avec le jeu de différentes manières :

A. Sélection d'un personnage
Comment :
Le joueur clique sur un personnage avec le bouton gauche de la souris.
Si le clic est valide (cible sur un personnage), celui-ci est sélectionné.
Effet :
Le personnage sélectionné est enregistré dans la variable personnage_selectionne.
Ses informations sont affichées dans le bandeau inférieur.
B. Déplacement du personnage
Comment :
Le joueur utilise les flèches directionnelles (K_UP, K_DOWN, K_LEFT, K_RIGHT).
Chaque pression déplace le personnage sélectionné d’une case dans la direction correspondante.
Effet :
Le personnage se déplace sur la grille, en actualisant ses coordonnées.
C. Utilisation des compétences
Comment :
Le joueur appuie sur la touche Espace après avoir sélectionné un personnage.
Un menu de compétences s'affiche dans la console (pour simplifier).
Le joueur entre le numéro de la compétence à utiliser.
Effet :
La compétence choisie est exécutée :
Si la compétence est ciblée, elle affecte un ennemi spécifique.
Si elle est de zone, elle affecte plusieurs ennemis à portée.
D. Désélection
Comment :
Appuyer sur la touche Entrée désélectionne le personnage actif.
Effet :
Permet de sélectionner un autre personnage ou d'effectuer une autre action.
4. Gestion des compétences
Les compétences des personnages sont gérées de manière dynamique :

Lorsqu’un personnage utilise une compétence, le programme identifie le type de personnage (Chevalier, Archer, ou Mage) et propose un menu interactif.
Les cibles potentielles sont automatiquement déterminées en excluant le personnage actif et en vérifiant les ennemis en vie.
5. Gestion des PV et fin de partie
Chaque tour, le programme :

Vérifie les points de vie (pv) de chaque personnage.
Retire les personnages morts de la liste personnages.
Si un seul personnage reste, il est déclaré gagnant, et la boucle principale se termine.
6. Rendu graphique
Carte : Chargée depuis un fichier TMX pour représenter un terrain visuel interactif.
Grille : Affiche les cases du terrain sous la carte.
Personnages :
Chaque personnage est dessiné à sa position avec son sprite (image_path).
Les PV sont affichés au-dessus du personnage pour permettre au joueur de surveiller l’état des unités.
Bandeau inférieur :
Affiche les statistiques du personnage sélectionné (PV, attaque, défense).
Donne des informations utiles au joueur pendant la partie.
"""
