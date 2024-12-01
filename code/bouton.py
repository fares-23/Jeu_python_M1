import pygame

class Bouton:
    
    def __init__(self, text, x, y, width, height, couleur, image=None, image_survol=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.couleur = couleur
        self.image = image
        self.image_survol = image_survol
        if self.image:
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        if self.image_survol:
            self.image_survol = pygame.transform.smoothscale(self.image_survol, (width, height))
        
    def afficher(self, fenetre):
        if self.image_survol and self.rect.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(self.image_survol, self.rect)
        elif self.image:
            fenetre.blit(self.image, self.rect)
        else:
            pygame.draw.rect(fenetre, self.couleur, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        fenetre.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))
