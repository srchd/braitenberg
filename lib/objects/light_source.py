import pygame

from lib.objects.drawable_object import DrawableObject
from lib.utils import create_multi_dimensional_fading_array


class LightSource(DrawableObject):
    def __init__(self, x, y, img_path, radius) -> None:
        """
        Initializes the LightSource class.
        Calls the parent 'DrawableObject' constructor.
        Sets the radius and the alpha-array to create a fading effect.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
        """
        super().__init__(x, y, img_path)

        self.radius = radius
        # size = radius * 2 + 1 -> the length of the rectangle
        self.alpha_array = create_multi_dimensional_fading_array(self.radius * 2 + 1, 255, 125)

        self.light_sources = []

    def draw(self, surface: pygame.Surface, scaling_factor: float) -> None:
        """
        Draws the LightSource.

        Parameters:
            surface (pygame.Surface): The surface where the LightSource should be drawn.
            scaling_factor (float): Represents how much should we scale up the image.
        """

        # Scaling up the image
        image_width = 1.0
        image_height = 1.0
        base_image_width = int(image_width * scaling_factor)
        base_image_height = int(image_height * scaling_factor)
        light_source = pygame.transform.scale(self.img, (base_image_width, base_image_height))

        # Setting the values for the loop
        start_x = int((self.x - light_source.get_width() / 2) - self.radius * light_source.get_width())
        start_y = int((self.y - light_source.get_height() / 2) - self.radius * light_source.get_height())

        end_x = int((self.x + light_source.get_width() / 2) + self.radius * light_source.get_width())
        end_y = int((self.y + light_source.get_height() / 2) + self.radius * light_source.get_height())

        for x in range(start_x, end_x, light_source.get_width()):
            for y in range(start_y, end_y, light_source.get_height()):
                alpha_x = int((x - start_x) / light_source.get_width())
                alpha_y = int((y - start_y) / light_source.get_width())

                # Need to copy a surface, otherwise all the alpha values would be the last one.
                plotting_light = light_source.copy()

                plotting_light.set_alpha(self.alpha_array[alpha_x, alpha_y])

                rect = plotting_light.get_rect()
                rect.centerx = x
                rect.centery = y
                self.light_sources.append((plotting_light, rect))

                surface.blit(plotting_light, (x, y))

        return