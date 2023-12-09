import pygame
from abc import ABC

class DrawableObject:
    """
    Parent class of all drawable objects
    """ 
    def __init__(self, x, y, img_path) -> None:
        self.x = x
        self.y = y
        self.img_path = img_path

        self.rotation = 0  # Facing upwards
        self._load_object_image()

    def _load_object_image(self) -> None:
        self.img = pygame.image.load(self.img_path)

    def rotate_object(self, rotation) -> None:
        self.rotation += rotation
        if self.rotation > 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360
