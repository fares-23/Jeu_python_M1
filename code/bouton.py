import pygame

class Bouton:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.couleur_contour = (0, 0, 0)  # couleur noire par défaut
        self.couleur_contour_survol = (255, 0, 0)  # couleur rouge pour le survol

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(fenetre, self.couleur_contour, (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        fenetre.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))

    def mettre_en_survol(self, fenetre, event):
        if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
            self.couleur_contour = self.couleur_contour_survol
        else:
            self.couleur_contour = (0, 0, 0)


