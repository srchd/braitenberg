import pygame
import numpy as np

from lib.objects.drawable_object import DrawableObject
from lib.utils import create_multi_dimensional_fading_array


class LightSource(DrawableObject):
    def __init__(self, x, y, img_path, radius) -> None:
        super().__init__(x, y, img_path)

        self.radius = radius

    def draw(self, surface: pygame.Surface, scaling_factor) -> None:
        image_width = 1.0
        image_height = 1.0
        base_image_width = int(image_width * scaling_factor)
        base_image_height = int(image_height * scaling_factor)
        light_source = pygame.transform.scale(self.img, (base_image_width, base_image_height))
        
        new_rect = light_source.get_rect()
        new_rect.centerx = self.x
        new_rect.centery = self.y

        surface.blit(light_source, new_rect)

        alpha_array = create_multi_dimensional_fading_array(self.radius * 2 + 1, 255, 125)

        start_x = int((self.x - light_source.get_width() / 2) - self.radius * light_source.get_width())
        start_y = int((self.y - light_source.get_height() / 2) - self.radius * light_source.get_height())

        end_x = int((self.x + light_source.get_width() / 2) + self.radius * light_source.get_width())
        end_y = int((self.y + light_source.get_height() / 2) + self.radius * light_source.get_height())

        for x in range(start_x, end_x, light_source.get_width()):
            for y in range(start_y, end_y, light_source.get_height()):
                light_source.set_alpha(alpha_array[int((x - start_x) / light_source.get_width()), int((y - start_y) / light_source.get_width())])
                surface.blit(light_source, (x, y))