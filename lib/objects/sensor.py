import pygame

from lib.objects.drawable_object import DrawableObject
from lib.objects.car import Car
from lib.objects.light_source import LightSource


class Sensor(DrawableObject):
    def __init__(self, x: int, y: int, img_path: str, offset_vector: tuple) -> None:
        """
        Initializes the Sensor class.
        Calls the parent 'DrawableObject' constructor.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
            offset_vector (pygame.math.Vector2): The offset 2D Vector from the pivot (car) point.
        """
        super().__init__(x, y, img_path)

        self.offset_vector = offset_vector
        self.rotation_to_car_offset = 90

        return
    
    def draw(self, car: Car, surface: pygame.Surface) -> None:
        """
        Draws the Sensor, and rotating them pivoting the car's center point

        Parameters:
            car (Car): The car, where the sensors are attached.
            surface (pygame.Surface): The surface where the sensors have to be drawn.
        """

        # Adding the Car's rotation, since the original images have a difference in rotation
        self.rotation = car.rotation + self.rotation_to_car_offset


        # Rotates the image, the offset vector, and adding the vector to the pivot point
        rotated_image = pygame.transform.rotozoom(self.img, self.rotation, 1)
        rotated_offset = self.offset_vector.rotate(-self.rotation)
        self.rect = rotated_image.get_rect(center=(car.x, car.y)+rotated_offset)

        pygame.draw.rect(surface, (0, 255, 0), self.rect)

        surface.blit(rotated_image, self.rect)

        return
    
    def check_light(self, light_sources: list[(LightSource, pygame.Rect)]) -> int:
        """
        Checks the sorruinding for light. Returns the alpha value, if found, otherwise 0.

        Parameters:
            light_sources (list[(LightSource, pygame.Rect)]): A list of (LightSource, rect) tuples. Checks the rect for collision.

        Returns:
            alpha (int): The alpha value for the collided LightSource.
        """
        alpha = 0

        for light_source, rect in light_sources:
            light_rect = rect

            if self.rect.colliderect(light_rect):
                alpha = max(light_source.get_alpha(), alpha)

        return alpha
