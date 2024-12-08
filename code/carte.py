import pygame
from pytmx import load_pygame
from constante import *

class Carte:
    def __init__(self, fichier_tmx, offset_x=0, offset_y=0):
        self.offset_x = offset_x
        self.offset_y = offset_y
        try:
            self.tmx_data = load_pygame(fichier_tmx)
            print(f"Carte {fichier_tmx} chargée avec succès.")
        except Exception as e:
            print(f"Erreur lors du chargement de la carte : {e}")
            raise e

        # Dictionnaire pour stocker les coordonnées des zones par calque
        self.zones = {}
        self.extraire_coordonnees_par_calque()

    def extraire_coordonnees_par_calque(self):
        """Parcourt les calques et extrait les coordonnées pour chaque calque."""
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, "name") and hasattr(layer, "tiles"):
                zone_coords = []  # Liste pour stocker les coordonnées des tuiles de ce calque
                for x, y, tile in layer.tiles():
                    if tile:  # Si la tuile existe
                        zone_coords.append((x*TAILLE_CASE, y*TAILLE_CASE))  # Ajoute les coordonnées (x, y) de la tuile
                # Ajoute ces coordonnées à l'attribut 'zones' sous le nom du calque
                self.zones[layer.name] = zone_coords
                #print(f"Calque '{layer.name}' : {len(zone_coords)} tuiles trouvées.")
                #print(f"coordonnées du calque '{layer.name}' : {zone_coords}")


    def afficher(self, fenetre):
        """Affiche tous les calques visibles."""
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, "tiles"):
                for x, y, tile in layer.tiles():
                    if tile:
                        fenetre.blit(tile, (x * self.tmx_data.tilewidth + self.offset_x,
                                            y * self.tmx_data.tileheight + self.offset_y))

    def recuperer_coordonnees_calque(self, nom_calque):
        """
        Récupère toutes les coordonnées des tuiles dans un calque donné.
        :param nom_calque: Le nom du calque (exemple : 'eau', 'arbre', etc.)
        :return: Liste des coordonnées (x, y) des tuiles dans ce calque.
        """
        if nom_calque in self.zones:
            return self.zones[nom_calque]
        else:
            #print(f"Le calque '{nom_calque}' n'existe pas.")
            return []
