from royaume import Royaume
import pygame
import random
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from constante import *

# La classe Saint_Royaume_de_Faerghus représente un royaume spécifique dans le jeu. 
# Elle hérite de la classe abstraite Royaume, et elle définit une armée spécifique à ce royaume.
class Saint_Royaume_de_Faerghus(Royaume):
    
    # Le constructeur initialise le nom du royaume et les probabilités d'apparition de chaque type d'unité (mage, chevalier, archer).
    def __init__(self):
        self.nom = "Empire Adrastien"  # Nom du royaume
        self.__prob_mage = 0.5  # Probabilité d'avoir des mages dans l'armée
        self.__prob_chevalier = 0.2  # Probabilité d'avoir des chevaliers dans l'armée
        self.__prob_archer = 0.3  # Probabilité d'avoir des archers dans l'armée
        self.__troupe = []  # Liste des unités (troupe) du royaume

    # La méthode armee génère une armée aléatoire en fonction des probabilités définies et positionne les unités.
    # Elle prend en entrée une liste de coordonnées (liste_coordonees) pour placer chaque unité sur la carte.
    def armee(self, liste_coordonees):
        # Génère une armée en choisissant entre chevaliers, archers et mages selon les probabilités.
        armee = random.choices(["chevalier", "archer", "mage"], weights=[self.__prob_chevalier, self.__prob_archer, self.__prob_mage], k=nb_troupe)
        
        # Crée les unités et les ajoute à la liste de troupe en fonction du type généré.
        for i in range(len(armee)):
            if armee[i] == "chevalier":  # Si l'unité est un chevalier
                self.__troupe.append(Chevalier(liste_coordonees[i][0], liste_coordonees[i][1], chevalier_b_path, "Saint Royaume de Faerghus"))
            elif armee[i] == "archer":  # Si l'unité est un archer
                self.__troupe.append(Archer(liste_coordonees[i][0], liste_coordonees[i][1], archer_b_path, "Saint Royaume de Faerghus"))
            elif armee[i] == "mage":  # Si l'unité est un mage
                self.__troupe.append(Mage(liste_coordonees[i][0], liste_coordonees[i][1], mage_b_path, "Saint Royaume de Faerghus"))
    
    # La propriété 'troupe' permet d'accéder à la liste des unités du royaume.
    # Elle est définie avec @property pour permettre un accès facile à la liste sans avoir à appeler une méthode explicite.
    @property
    def troupe(self):
        return self.__troupe  # Retourne la liste des unités du royaume.
