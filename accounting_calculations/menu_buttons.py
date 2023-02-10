import pygame


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.count = 0

    def draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return False

    def toggle_draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True

        if not self.clicked:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return self.clicked

    def null_count(self):
        self.clicked = False