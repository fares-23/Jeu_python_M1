import pygame

class Bouton:
    def __init__(self, text, x, y, width, height, couleur, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.couleur = couleur
        self.image = image
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))
        
    def afficher(self, fenetre):
        if self.image:
            fenetre.blit(self.image, self.rect)
        else:
            pygame.draw.rect(fenetre, self.couleur, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        fenetre.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))

