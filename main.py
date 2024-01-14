# Python Modules Imports
import os
import sys
import tkinter as tk

# Extending PATH variable, to be able to detect libraries
root_dir = os.path.join(os.getcwd().split('braitenberg')[0], 'braitenberg')

sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'windows'))
sys.path.append(os.path.join(root_dir, 'lib'))

# Library Imports
from windows.main_window import MainWindow
from windows.config_window import ConfigWindow

def main() -> None:
    # master = tk.Tk()
    # master.withdraw()
    config_window = ConfigWindow(master=tk.Tk())
    config_window.run()

    main_win = MainWindow()
    main_win.run(save_frequency=300)

    return

if __name__ == '__main__':
    main()
