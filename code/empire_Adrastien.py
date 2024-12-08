import pygame
import random
from royaume import Royaume
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from constante import *

class Empire_Adrastien(Royaume):
    def __init__(self):
        self.__nom = "Empire Adrastien"
        self.__prob_mage = 0.3
        self.__prob_chevalier = 0.4
        self.__prob_archer = 0.3
        self.__troupe = []
        
    
    def armee(self,liste_coordonees):
        #gernère une armée aléatoire réparti entre chevalier/mage/archer
        armee = random.choices(["chevalier", "archer", "mage"], weights=[self.__prob_chevalier, self.__prob_archer, self.__prob_mage], k=nb_troupe)
        for i in range(len(armee)):
            if armee[i] == "chevalier":
                self.__troupe.append(Chevalier(liste_coordonees[i][0],liste_coordonees[i][1],chevalier_r_path,"Empire Adrastien"))
            elif armee[i] == "archer":
                self.__troupe.append(Archer(liste_coordonees[i][0],liste_coordonees[i][1],archer_r_path,"Empire Adrastien"))
            elif armee[i] == "mage":
                self.__troupe.append(Mage(liste_coordonees[i][0],liste_coordonees[i][1],mage_r_path,"Empire Adrastien"))
    
    @property
    def troupe(self):
        return self.__troupe
        