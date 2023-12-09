import pygame

def draw_checkerboard_background(surface: pygame.Surface, checkerboard_image, scaling_factor):
    image_width = 2.0
    image_height = 2.0
    base_image_width = int(image_width * scaling_factor)
    base_image_height = int(image_height * scaling_factor)
    checkerboard = pygame.transform.scale(checkerboard_image, (base_image_width, base_image_height))

    # x_start
    for x in range(0, surface.get_width(), checkerboard.get_width()):
        for y in range(0, surface.get_height(), checkerboard.get_height()):
            surface.blit(checkerboard, (x, y))
