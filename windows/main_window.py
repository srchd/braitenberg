import pygame


class MainWindow:
    def __init__(self, size: tuple=(500, 500), title: str='Braitenberg Vehicle') -> None:
        self.size = size
        self.title = title

        self._initialize_pygame_window()

    def _initialize_pygame_window(self) -> None:
        self.canvas = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def run(self) -> None:
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            pygame.display.update()
