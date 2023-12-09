# Python Modules Imports
import pygame

# Library Imports
from lib.pygame_plotter import *
from lib.objects.car import Car
from lib.objects.controller import Controller


class MainWindow:
    def __init__(self, size: tuple=(500, 500), title: str='Braitenberg Vehicle') -> None:
        self.size = size
        self.title = title
        self.scaling_factor = float(50)

        self._initialize_pygame_window()
        self._load_checkerboard_image()
        self._load_objects()

    def _initialize_pygame_window(self) -> None:
        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        # self.surface.fill((113, 113, 113))

    def _load_checkerboard_image(self) -> None:
        path_to_image = 'images/checkerboard.png'
        self.background_image = pygame.image.load(path_to_image)

    def _load_objects(self) -> None:
        path_to_car = 'images/car.png'
        car_x = 0  # self.surface.get_width() / 2
        car_y = 0  # self.surface.get_height() / 2
        self.car = Car(car_x, car_y, path_to_car, self.surface)

        path_to_controller = 'images/controller.png'
        self.controller = Controller(0, 0, path_to_controller)

    def run(self) -> None:
        finished = False

        pygame.init()

        clock = pygame.time.Clock()

        while not finished:
            clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.car.move(-20)
                    if event.key == pygame.K_s:
                        self.car.move(20)
                    if event.key == pygame.K_a:
                        self.car.rotate_object(10)
                    if event.key == pygame.K_d:
                        self.car.rotate_object(-10)

            draw_checkerboard_background(self.surface, self.background_image, self.scaling_factor)
            self.car.draw(self.surface)
            self.controller.draw(self.car)

            pygame.display.update()
