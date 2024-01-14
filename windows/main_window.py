# Python Modules Imports
import pygame
import os
from datetime import datetime
import json
from pathlib import Path

# Library Imports
from lib.pygame_plotter import *
from lib.objects.car import Car
from lib.objects.controller import Controller
from lib.objects.light_source import LightSource
from lib.objects.sensor import Sensor
from lib.enum_types import Wirings
from lib.configuration import Configuration


class MainWindow:
    def __init__(self, title: str='Braitenberg Vehicle') -> None:
        """
        Initializes the MainWindow class.

        Parameters:
            size (tuple): Width and Height values for the window.
            title (str): Window title.
        """
        configuration = Configuration()
        temp_config_path = os.path.join(Configuration.CONFIGS_DIR, 'temp.yml')

        if os.path.isfile(temp_config_path):
            config_dict = configuration.parse_config(temp_config_path)
            os.remove(temp_config_path)
        else:
            config_path = os.path.join(Configuration.CONFIGS_DIR, 'defaultconfig.yml')
            config_dict = configuration.parse_config(config_path)

        self.size = (config_dict['width'], config_dict['height'])
        self.title = title
        self.scaling_factor = float(50)

        self._initialize_pygame_window()
        self._load_checkerboard_image()
        self._load_objects(config_dict)
        self._initialize_recording(config_dict)
        self._initialize_replaying(config_dict)

    def _initialize_pygame_window(self) -> None:
        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def _initialize_recording(self, config_dict) -> None:
        self.record_scene = config_dict['record_scene']
        if self.record_scene:
            self.recorded_data = dict()
            self.recorded_data['width'] = self.size[0]
            self.recorded_data['height'] = self.size[1]
            self.recorded_data['light_source'] = self.light_source_radius
            self.recorded_data['record_scene'] = self.record_scene

            self.recorded_data['light_source_positions'] = list()

    def _initialize_replaying(self, config_dict) -> None:
        self.light_source_positions = config_dict.get('light_source_positions', None)

        if self.light_source_positions is None:
            self.is_replaying = False
        else:
            self.is_replaying = True

    def _load_checkerboard_image(self) -> None:
        path_to_image = 'images/checkerboard.png'
        self.background_image = pygame.image.load(path_to_image)

    def _load_objects(self, config_dict) -> None:
        path_to_car = 'images/car.png'
        car_x = self.surface.get_width()
        car_y = self.surface.get_height()
        self.car = Car(car_x, car_y, path_to_car)

        path_to_controller = 'images/controller.png'
        self.controller = Controller(0, 0, path_to_controller)

        self.light_source_radius = config_dict['light_source']
        self.path_to_light_source = 'images/light_source.png'
        self.light_source = LightSource(333, 333, self.path_to_light_source, self.light_source_radius)

        path_to_sensor = 'images/sensor.png'
        left_sensor_offset_vector = pygame.math.Vector2(40, 150)  # Offset vector form the center of the car
        self.left_sensor = Sensor(0, 0, path_to_sensor, left_sensor_offset_vector)

        right_sensor_offset_vector = pygame.math.Vector2(-40, 150)  # Offset vector form the center of the car
        self.right_sensor = Sensor(0, 0, path_to_sensor, right_sensor_offset_vector)

    def _save_scene(self) -> None:
        now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        json_file_name = f'{now}.json'
        json_file_path = os.path.join(Configuration.LOG_DIR, json_file_name)

        with open(json_file_path, 'w') as f:
            json.dump(self.recorded_data, f)

    def run(self, save_frequency=300) -> None:
        """
        Main function, which runs the simulation.
        This will be in a infinite-loop, until the 'X' pressed on the window.
        """
        finished = False

        pygame.init()

        clock = pygame.time.Clock()

        paused = False

        time_elapsed_in_ms = 0
        while not finished:
            dt = clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.is_replaying:
                        paused = not paused

                if event.type == pygame.MOUSEBUTTONDOWN and not self.is_replaying:
                    if event.button == 3:
                        mouse_pos = pygame.mouse.get_pos()
                        self.light_source = LightSource(mouse_pos[0], mouse_pos[1], self.path_to_light_source, self.light_source_radius)
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

            if self.is_replaying:
                time_elapsed_in_ms += dt
                current_index = time_elapsed_in_ms // save_frequency
                if current_index <= len(self.light_source_positions) - 1:
                    current_positions = self.light_source_positions[current_index]
                    # self.light_source.x = current_positions[0]
                    # self.light_source.y = current_positions[1]
                    self.light_source = LightSource(current_positions[0], current_positions[1], self.path_to_light_source, self.light_source_radius)
                else:
                    self.car.stop()

            if self.record_scene and not paused:
                time_elapsed_in_ms += dt
                if time_elapsed_in_ms > save_frequency:
                    self.recorded_data['light_source_positions'].append([self.light_source.x,
                                                                         self.light_source.y])
                    time_elapsed_in_ms = 0

            draw_checkerboard_background(self.surface, self.background_image, self.scaling_factor)
            self.car.draw(self.surface)
            self.controller.draw(self.car)
            self.left_sensor.draw(self.car, self.surface)
            self.right_sensor.draw(self.car, self.surface)
            self.light_source.draw(self.surface, self.scaling_factor)
            
            if not self.car.has_stopped() and not paused:
                left_light = self.left_sensor.check_light(self.light_source.light_sources)
                right_light = self.right_sensor.check_light(self.light_source.light_sources)
                print(f"LEFT:    {left_light}      RIGHT:    {right_light}")
                self.controller.control_car(self.car, right_light, left_light, wiring=Wirings.CROSS)

            pygame.display.update()

        if self.record_scene:
            self._save_scene()
