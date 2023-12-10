import pygame
import pygame.gfxdraw
import math

from lib.objects.drawable_object import DrawableObject


class Car(DrawableObject):
    def __init__(self, x: int, y: int, img_path: str) -> None:
        """
        Initializes the Car class.
        Calls the parent 'DrawableObject' constructor.
        Sets the X and Y position, so the car starts at the bottom right corner.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
        """
        super().__init__(x, y, img_path)   

        self.x -= self.img.get_height() / 2
        self.y -= self.img.get_width() / 2
        self.rotation = 90
        self.stopped = False

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the car

        Parameters:
            surface (pygame.Surface): The surface where the car should be drawn.
        """
        rotated_img = pygame.transform.rotate(self.img, self.rotation)

        new_rect = rotated_img.get_rect()
        new_rect.centerx = self.x
        new_rect.centery = self.y

        surface.blit(rotated_img, new_rect)

        return

    def move(self, vel: int) -> None:
        """
        Moves the car.
        
        Parameters:
            vel (int): The unit (in pixel) the car goes forward/backward. 
                        If the value is > 0, the car goes backwards.
                        If the value is < 0, the car goes forwards.
        """
        self.x += vel * math.cos(math.radians(self.rotation + 180))
        self.y -= vel * math.sin(math.radians(self.rotation + 180))

        return
    
    def stop(self) -> None:
        """Stops the car"""
        self.stopped = True

    def has_stopped(self) -> bool:
        """
        Returns:
            self.stopped (bool): Represents if the car has stopped moving or not.
        """
        return self.stopped
