import pygame

from lib.objects.drawable_object import DrawableObject
from lib.objects.car import Car

class Controller(DrawableObject):
    def __init__(self, x, y, img_path) -> None:
        super().__init__(x, y, img_path)

    def draw(self, car: Car) -> None:
        new_rect = self.img.get_rect()
        new_rect.centerx = 240
        new_rect.centery = 62

        car.img.blit(self.img, new_rect)
