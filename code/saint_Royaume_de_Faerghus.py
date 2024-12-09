from royaume import Royaume
import pygame
import random
from archer import Archer
from mage import Mage
from chevalier import Chevalier
from constante import *

class Saint_Royaume_de_Faerghus(Royaume):
    def __init__(self):
        self.nom = "Empire Adrastien"
        
        self.__prob_mage = 0.5
        self.__prob_chevalier = 0.2
        self.__prob_archer = 0.3
        self.__troupe = []
        
    
    def armee(self,liste_coordonees):
        #gernère une armée aléatoire réparti entre chevalier/mage/archer
        armee = random.choices(["chevalier", "archer", "mage"], weights=[self.__prob_chevalier, self.__prob_archer, self.__prob_mage], k=nb_troupe)
        for i in range(len(armee)):
            if armee[i] == "chevalier":
                self.__troupe.append(Chevalier(liste_coordonees[i][0],liste_coordonees[i][1],chevalier_b_path,"Saint Royaume de Faerghus"))
            elif armee[i] == "archer":
                self.__troupe.append(Archer(liste_coordonees[i][0],liste_coordonees[i][1],archer_b_path,"Saint Royaume de Faerghus"))
            elif armee[i] == "mage":
                self.__troupe.append(Mage(liste_coordonees[i][0],liste_coordonees[i][1],mage_b_path,"Saint Royaume de Faerghus"))
    
    @property
    def troupe(self):
        return self.__troupe
        
    
    