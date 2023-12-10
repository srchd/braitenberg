# Python Modules Imports
import pygame

# Library Imports
from lib.pygame_plotter import *
from lib.objects.car import Car
from lib.objects.controller import Controller
from lib.objects.light_source import LightSource
from lib.objects.sensor import Sensor


class MainWindow:
    def __init__(self, size: tuple=(500, 500), title: str='Braitenberg Vehicle') -> None:
        """
        Initializes the MainWindow class.

        Parameters:
            size (tuple): Width and Height values for the window.
            title (str): Window title.
        """
        self.size = size
        self.title = title
        self.scaling_factor = float(50)

        self._initialize_pygame_window()
        self._load_checkerboard_image()
        self._load_objects()

    def _initialize_pygame_window(self) -> None:
        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def _load_checkerboard_image(self) -> None:
        path_to_image = 'images/checkerboard.png'
        self.background_image = pygame.image.load(path_to_image)

    def _load_objects(self) -> None:
        path_to_car = 'images/car.png'
        car_x = self.surface.get_width()
        car_y = self.surface.get_height()
        self.car = Car(car_x, car_y, path_to_car)

        path_to_controller = 'images/controller.png'
        self.controller = Controller(0, 0, path_to_controller)

        path_to_light_source = 'images/light_source.png'
        self.light_source = LightSource(333, 333, path_to_light_source, 9)

        path_to_sensor = 'images/sensor.png'
        left_sensor_offset_vector = pygame.math.Vector2(40, 150)  # Offset vector form the center of the car
        self.left_sensor = Sensor(0, 0, path_to_sensor, left_sensor_offset_vector)

        right_sensor_offset_vector = pygame.math.Vector2(-40, 150)  # Offset vector form the center of the car
        self.right_sensor = Sensor(0, 0, path_to_sensor, right_sensor_offset_vector)

    def run(self) -> None:
        """
        Main function, which runs the simulation.
        This will be in a infinite-loop, until the 'X' pressed on the window.
        """
        finished = False

        pygame.init()

        clock = pygame.time.Clock()

        while not finished:
            clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                """
                Controlling with keyboard, only for testing purposes.
                """
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_w:
                #         self.car.move(-20)
                #     if event.key == pygame.K_s:
                #         self.car.move(20)
                #     if event.key == pygame.K_a:
                #         self.car.rotate_object(10)
                #     if event.key == pygame.K_d:
                #         self.car.rotate_object(-10)

            draw_checkerboard_background(self.surface, self.background_image, self.scaling_factor)
            self.car.draw(self.surface)
            self.controller.draw(self.car)
            self.left_sensor.draw(self.car, self.surface)
            self.right_sensor.draw(self.car, self.surface)
            self.light_source.draw(self.surface, self.scaling_factor)
            
            if not self.car.has_stopped():
                left_light = self.left_sensor.check_light(self.light_source.light_sources)
                right_light = self.right_sensor.check_light(self.light_source.light_sources)
                print(f"LEFT:    {left_light}      RIGHT:    {right_light}")
                self.controller.control_car(self.car, right_light, left_light)

            pygame.display.update()
