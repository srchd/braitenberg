# Python Modules Imports
import pygame

# Library Imports
from lib.pygame_plotter import *


class MainWindow:
    def __init__(self, size: tuple=(500, 500), title: str='Braitenberg Vehicle') -> None:
        self.size = size
        self.title = title
        self.scaling_factor = float(50)

        self._initialize_pygame_window()
        self._load_checkerboard_image()

    def _initialize_pygame_window(self) -> None:
        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        # self.surface.fill((113, 113, 113))

    def _load_checkerboard_image(self) -> None:
        path_to_image = 'images/checkerboard.png'
        self.background_image = pygame.image.load(path_to_image)

    def run(self) -> None:
        finished = False

        pygame.init()

        clock = pygame.time.Clock()

        while not finished:
            clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

            draw_checkerboard_background(self.surface, self.background_image, self.scaling_factor)

            pygame.display.update()
