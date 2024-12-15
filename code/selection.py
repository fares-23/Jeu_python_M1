import pygame
from constante import *
from menu import Menu
from bouton import Bouton
from empire_Adrastien import Empire_Adrastien
from saint_Royaume_de_Faerghus import Saint_Royaume_de_Faerghus
from alliance_de_Leicester import Alliance_de_Leicester

# La classe Selection gère la sélection des royaumes et la préparation des troupes au début du jeu.
# Elle permet à l'utilisateur de choisir deux royaumes et de lancer le jeu avec les troupes des royaumes sélectionnés.
class Selection:
    
    # Le constructeur initialise les éléments nécessaires à l'affichage de l'interface de sélection.
    def __init__(self, fenetre):
        self.fenetre = fenetre  # Fenêtre de jeu où la sélection sera affichée
        self.police = pygame.font.SysFont("Arial", 30)  # Police utilisée pour afficher le texte sur les boutons
        # Chargement des images pour les boutons du menu
        self.image = [pygame.image.load("assets/interface/MenuButtonPreLight.png"),
                      pygame.image.load("assets/interface/item_frame.png")]
        
        # Création des boutons pour sélectionner un royaume et le bouton "Suivant"
        self.boutons = [Bouton("Empire Adrastien", 75, 100, 250, 50, NOIR, self.image[1]),
                        Bouton("Saint Royaume de Faerghus", 375, 100, 400, 50, NOIR, self.image[1]),
                        Bouton("Alliance de Leicester", 820, 100, 300, 50, NOIR, self.image[1]),
                        Bouton("Suivant", self.fenetre.get_width() // 2 - 100, self.fenetre.get_height() // 2 + 200, 200, 50, NOIR, self.image[0])]
        
        # Listes pour stocker les royaumes et troupes sélectionnés
        self.royaumes_selectionnes = []
        self.liste_royaume = []
        self.liste_troupe = []
        
        # Chargement des images des blasons des royaumes
        self.images = [pygame.transform.smoothscale(pygame.image.load("assets/blason/Adrestian_crest.webp"), (200, 200)),
                       pygame.transform.smoothscale(pygame.image.load("assets/blason/Faerghus_crest.webp"), (200, 200)),
                       pygame.transform.smoothscale(pygame.image.load("assets/blason/Leicester_crest.webp"), (200, 200))]

        # Positionnement des images des blasons sur l'écran
        self.images_rect = [self.images[0].get_rect(topleft=(100, 200)), 
                            self.images[1].get_rect(topleft=(480, 200)), 
                            self.images[2].get_rect(topleft=(870, 200))]
        
    # La méthode dessiner gère l'affichage des boutons et des blasons des royaumes sur la fenêtre.
    def dessiner(self, fenetre):
        # Affiche tous les boutons sauf le bouton "Suivant" tant que deux royaumes n'ont pas été sélectionnés
        for i in range(len(self.boutons)-1):
            self.boutons[i].afficher(fenetre)
        # Si deux royaumes ont été sélectionnés, le bouton "Suivant" est affiché
        if len(self.royaumes_selectionnes) == 2:
            self.boutons[3].afficher(fenetre)
        # Affiche les blasons des royaumes lorsque la souris survole un bouton ou que le royaume est sélectionné
        for i, image in enumerate(self.images):
            # Si la souris survole le bouton ou si le royaume est sélectionné, affiche l'image correspondante
            if self.boutons[i].rect.collidepoint(pygame.mouse.get_pos()) or self.boutons[i].text in self.royaumes_selectionnes:
                fenetre.blit(image, self.images_rect[i])
    
    # La méthode gerer_evenements gère les événements de clic sur les boutons et permet de sélectionner des royaumes.
    def gerer_evenements(self, event, coord_start):
        # Vérifie si un bouton a été cliqué
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si le bouton "Empire Adrastien" est cliqué, on ajoute ou retire le royaume de la sélection
            if self.boutons[0].rect.collidepoint(event.pos):
                if "Empire Adrastien" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Empire Adrastien")
                    self.liste_royaume.remove("Empire Adrastien")
                else:
                    self.royaumes_selectionnes.append("Empire Adrastien")
                    self.liste_royaume.append("Empire Adrastien")
            # Si le bouton "Saint Royaume de Faerghus" est cliqué, on ajoute ou retire le royaume de la sélection
            elif self.boutons[1].rect.collidepoint(event.pos):
                if "Saint Royaume de Faerghus" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Saint Royaume de Faerghus")
                    self.liste_royaume.remove("Saint Royaume de Faerghus")
                else:
                    self.royaumes_selectionnes.append("Saint Royaume de Faerghus")
                    self.liste_royaume.append("Saint Royaume de Faerghus")
            # Si le bouton "Alliance de Leicester" est cliqué, on ajoute ou retire le royaume de la sélection
            elif self.boutons[2].rect.collidepoint(event.pos):
                if "Alliance de Leicester" in self.royaumes_selectionnes:
                    self.royaumes_selectionnes.remove("Alliance de Leicester")
                    self.liste_royaume.remove("Alliance de Leicester")
                else:
                    self.royaumes_selectionnes.append("Alliance de Leicester")
                    self.liste_royaume.append("Alliance de Leicester")
                    
            # Si le bouton "Suivant" est cliqué et deux royaumes ont été sélectionnés, la méthode suivante est appelée
            elif self.boutons[3].rect.collidepoint(event.pos) and len(self.royaumes_selectionnes) == 2:
                # Pour chaque royaume sélectionné, créer une instance et générer l'armée
                for i in range(len(self.royaumes_selectionnes)):
                    if self.royaumes_selectionnes[i] == "Empire Adrastien":
                        self.royaumes_selectionnes[i] = Empire_Adrastien()
                        self.royaumes_selectionnes[i].armee(coord_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                    elif self.royaumes_selectionnes[i] == "Saint Royaume de Faerghus":
                        self.royaumes_selectionnes[i] = Saint_Royaume_de_Faerghus()
                        self.royaumes_selectionnes[i].armee(coord_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                    elif self.royaumes_selectionnes[i] == "Alliance de Leicester":
                        self.royaumes_selectionnes[i] = Alliance_de_Leicester()
                        self.royaumes_selectionnes[i].armee(coord_start[i])
                        self.liste_troupe += self.royaumes_selectionnes[i].troupe
                return "jeu"  # Retourne "jeu" pour démarrer la partie
                    
        return "selection"  # Retourne "selection" si les royaumes n'ont pas encore été sélectionnés
