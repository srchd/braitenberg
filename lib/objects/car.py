import pygame
import pygame.gfxdraw
import math

from lib.objects.drawable_object import DrawableObject


class Car(DrawableObject):
    def __init__(self, x, y, img_path, surface: pygame.Surface) -> None:
        super().__init__(x, y, img_path)   

        self.x = surface.get_width() / 2 # - self.img.get_height() / 2
        self.y = surface.get_height() / 2 # - self.img.get_width() / 2

    def draw(self, surface: pygame.Surface):
        rotated_img = pygame.transform.rotate(self.img, self.rotation)

        new_rect = rotated_img.get_rect()
        new_rect.centerx = self.x
        new_rect.centery = self.y

        surface.blit(rotated_img, new_rect)

    def move(self, vel):
        self.x += vel * math.cos(math.radians(self.rotation + 180))
        self.y -= vel * math.sin(math.radians(self.rotation + 180))
