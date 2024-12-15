import pygame
import random
from royaume import Royaume
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from constante import *

class Empire_Adrastien(Royaume):
    
    # Le constructeur initialise le royaume "Empire Adrastien" avec des probabilités pour chaque type d'unité (mage, chevalier, archer).
    def __init__(self):
        self.__nom = "Empire Adrastien"  # Le nom du royaume
        self.__prob_mage = 0.3  # Probabilité d'avoir des mages dans l'armée
        self.__prob_chevalier = 0.4  # Probabilité d'avoir des chevaliers dans l'armée
        self.__prob_archer = 0.3  # Probabilité d'avoir des archers dans l'armée
        self.__troupe = []  # Liste des unités qui composent l'armée du royaume
        
    # La méthode armee génère une armée aléatoire pour le royaume en fonction des probabilités définies ci-dessus.
    # Elle prend en entrée une liste de coordonnées (liste_coordonees) pour positionner les unités sur la carte.
    def armee(self, liste_coordonees):
        # Génère une armée aléatoire en choisissant parmi chevalier, archer et mage, selon les probabilités.
        armee = random.choices(["chevalier", "archer", "mage"], weights=[self.__prob_chevalier, self.__prob_archer, self.__prob_mage], k=nb_troupe)
        
        # Pour chaque unité générée, on crée une instance de la classe correspondante (Chevalier, Archer, Mage) et on l'ajoute à la troupe.
        for i in range(len(armee)):
            if armee[i] == "chevalier":  # Si l'unité est un chevalier
                self.__troupe.append(Chevalier(liste_coordonees[i][0], liste_coordonees[i][1], chevalier_r_path, "Empire Adrastien"))
            elif armee[i] == "archer":  # Si l'unité est un archer
                self.__troupe.append(Archer(liste_coordonees[i][0], liste_coordonees[i][1], archer_r_path, "Empire Adrastien"))
            elif armee[i] == "mage":  # Si l'unité est un mage
                self.__troupe.append(Mage(liste_coordonees[i][0], liste_coordonees[i][1], mage_r_path, "Empire Adrastien"))
    
    # La propriété 'troupe' permet d'accéder à la liste des unités de l'armée du royaume.
    # Elle est définie avec @property pour que l'accès à __troupe soit effectué comme si c'était un attribut direct.
    @property
    def troupe(self):
        return self.__troupe  # Retourne la liste des unités (troupe) du royaume.
