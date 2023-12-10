import pygame

class DrawableObject:
    """
    Parent class of all drawable objects
    """ 
    def __init__(self, x: int, y: int, img_path: str) -> None:
        """
        Initializes the DrawableObject class.

        Parameters:
            x (int): X position of the object.
            y (int): Y position of the object.
            img_path (str): The path to the image which represents the object.
        """
        self.x = x
        self.y = y
        self.img_path = img_path

        self.rotation = 0  # Facing upwards
        self._load_object_image()

    def _load_object_image(self) -> None:
        """Loads the image and saves it as a pygame object."""
        self.img = pygame.image.load(self.img_path)

    def rotate_object(self, rotation: int) -> None:
        """
        Rotates the object.
        
        Parameters:
            rotation (int): The amount the object has to be rotated.
                            If the value is > 0, rotation is counter-clockwise.
                            If the value is < 0, the rotation is clockwise.
        """
        self.rotation += rotation
        if self.rotation > 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360
