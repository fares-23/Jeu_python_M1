import pygame

class Bouton:
    
    def __init__(self, text, x, y, width, height, couleur, image=None, image_survol=None):
        # Création d'un rectangle représentant les dimensions et la position du bouton sur l'écran.
        self.rect = pygame.Rect(x, y, width, height)
        
        # Le texte affiché sur le bouton.
        self.text = text
        
        # Les coordonnées x et y du bouton.
        self.x = x
        self.y = y
        
        # La largeur et la hauteur du bouton.
        self.width = width
        self.height = height
        
        # La couleur du bouton (si aucune image n'est utilisée).
        self.couleur = couleur
        
        # Les images associées au bouton pour les états normaux et au survol (facultatives).
        self.image = image
        self.image_survol = image_survol
        
        # Si une image est spécifiée, elle est redimensionnée à la taille du bouton.
        if self.image:
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        
        # Si une image pour l'état de survol est spécifiée, elle est également redimensionnée.
        if self.image_survol:
            self.image_survol = pygame.transform.smoothscale(self.image_survol, (width, height))
        
    # La méthode afficher dessine le bouton sur la fenêtre.
    def afficher(self, fenetre):
        # Vérifie si la souris est sur le bouton (état de survol) et affiche l'image de survol si elle existe.
        if self.image_survol and self.rect.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(self.image_survol, self.rect)  # Affiche l'image de survol
        # Si une image est définie pour l'état normal, elle est affichée.
        elif self.image:
            fenetre.blit(self.image, self.rect)  # Affiche l'image normale
        else:
            # Si aucune image n'est définie, un rectangle de couleur est dessiné à la place.
            pygame.draw.rect(fenetre, self.couleur, self.rect)
        
        # Définir la police du texte à afficher (taille 36).
        font = pygame.font.Font(None, 36)
        
        # Crée une surface contenant le texte du bouton, en couleur blanche.
        text = font.render(self.text, True, (255, 255, 255))
        
        # Affiche le texte au centre du rectangle du bouton.
        fenetre.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))
