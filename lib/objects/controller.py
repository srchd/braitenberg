import pygame

from lib.objects.drawable_object import DrawableObject
from lib.objects.car import Car

class Controller(DrawableObject):
    def __init__(self, x, y, img_path) -> None:
        """
        Initializes the Controller class.
        Calls the parent 'DrawableObject' constructor.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
        """
        super().__init__(x, y, img_path)

    def draw(self, car: Car) -> None:
        """
        Draws the Controller.

        Parameters:
            car (Car): The car where the Controller is drawn.
        """
        new_rect = self.img.get_rect()

        # "Randomly" selected positions related to the car
        new_rect.centerx = 220
        new_rect.centery = 62

        car.img.blit(self.img, new_rect)

        return
