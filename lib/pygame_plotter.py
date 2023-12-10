import pygame

def draw_checkerboard_background(surface: pygame.Surface, checkerboard_image: pygame.Surface, scaling_factor: float) -> None:
    """
    Draws the checkerboard background from the 2x2 (in pixel) image.

    Parameters:
        surface (pygame.Surface): The surface where the checkerboard should be drawn.
        checkerboard_image (pygame.Surface): The loaded image of the background.
        scaling_factor (float): Represents how much should we scale up the image.
    """
    
    # Scaling up the image
    image_width = 2.0
    image_height = 2.0
    base_image_width = int(image_width * scaling_factor)
    base_image_height = int(image_height * scaling_factor)
    checkerboard = pygame.transform.scale(checkerboard_image, (base_image_width, base_image_height))

    for x in range(0, surface.get_width(), checkerboard.get_width()):
        for y in range(0, surface.get_height(), checkerboard.get_height()):
            surface.blit(checkerboard, (x, y))

    return
