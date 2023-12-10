import pygame

from lib.objects.drawable_object import DrawableObject
from lib.objects.car import Car

class Controller(DrawableObject):
    def __init__(self, x, y, img_path) -> None:
        """
        Initializes the Controller class.
        Calls the parent 'DrawableObject' constructor.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
        """
        super().__init__(x, y, img_path)

    def draw(self, car: Car) -> None:
        """
        Draws the Controller.

        Parameters:
            car (Car): The car where the Controller is drawn.
        """
        new_rect = self.img.get_rect()

        # "Randomly" selected positions related to the car
        new_rect.centerx = 220
        new_rect.centery = 62

        car.img.blit(self.img, new_rect)

        return
    
    def control_car(self, car: Car, right_light, left_light) -> None:
        """
        Controls the Car. (Ideally the wheels, this might need to be refactored in such a way).
        Steers the car towards the light, and moves it a little as well.
        If both the sensors are reading the same light, the car only goes forward.

        Parameters:
            car (Car): The car in question.
            right_light (int): The alpha value readed from the right light sensor.
            left_light (int): The alpha value readed from the left light sensor.
        """
        if right_light > left_light:
            car.rotate_object(-1)
            car.move(-1)
        elif right_light < left_light:
            car.rotate_object(1)
            car.move(-1)

        # Standard movement, going in circles, I call it idle movement.
        elif right_light == 0 and left_light == 0:
            car.rotate_object(1)
            car.move(-2)
        else:
            car.move(-5)

            # If both sensors read the same 255 value, the car stops.
            if right_light == 255 and left_light == 255:
                car.stop()

        return
