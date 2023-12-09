# Python Modules Imports
import pygame
import os
import sys

# Extending PATH variable, to be able to detect libraries
root_dir = os.path.join(os.getcwd().split('braitenberg')[0], 'braitenberg')

sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'windows'))

# Library Imports
from windows.main_window import MainWindow

def main() -> None:
    pygame.init()

    main_win = MainWindow(size=(1200, 700))
    main_win.run()

    return

if __name__ == '__main__':
    main()
