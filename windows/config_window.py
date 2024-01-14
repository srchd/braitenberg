import tkinter as tk
from tkinter import filedialog
import os
import copy
import sys
import json

from lib.configuration import Configuration


class ConfigWindow(tk.Toplevel):
    def __init__(self, master) -> None:
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.on_close)
        self.title("Braitenberg Configuration")

        self.width = "400"
        self.height = "600"

        self.config_path = os.path.join(Configuration.CONFIGS_DIR, 'defaultconfig.yml')
        self.temp_config_path = os.path.join(Configuration.CONFIGS_DIR, 'temp.yml')
        self.configuration = Configuration()

        self._record_scene_var = tk.BooleanVar()

        self.geometry(self.get_window_size())

        self._initialize_components()
        self.load_config()

    def _initialize_components(self) -> None:
        self._initialize_light_source_frame()
        self._initialize_buttons_frame()
        self._initialize_custom_size_frame()
        self._initialize_save_load_config_frame()
        self._initialize_record_scene_frame()
        self._initialize_replay_screen_frame()

    def _initialize_light_source_frame(self) -> None:
        self.light_source_frame = tk.Frame(self)

        self.light_source_label = tk.Label(self.light_source_frame, padx=20, text='Radius of the Light Source:')
        self.light_source_slider = tk.Scale(self.light_source_frame, from_=4, to=10, tickinterval=1, orient=tk.HORIZONTAL)

        self.light_source_label.pack(side=tk.LEFT)
        self.light_source_slider.pack(side=tk.LEFT)

        self.light_source_frame.pack()

    def _initialize_buttons_frame(self) -> None:
        self.button_frame = tk.Frame(self)
        
        self.apply_button = tk.Button(self.button_frame, padx=20, pady=10, text='Apply', border=10)
        self.close_button = tk.Button(self.button_frame, padx=20, pady=10, text='Close', border=10)

        self.apply_button.pack(side=tk.LEFT)
        self.close_button.pack(side=tk.LEFT)

        self.button_frame.pack(side=tk.BOTTOM)

        self.apply_button.config(command=self.on_apply)
        self.close_button.config(command=self.on_close)

    def _initialize_custom_size_frame(self) -> None:
        self.custom_size_frame = tk.Frame(self)

        self.width_label = tk.Label(self.custom_size_frame, padx=20, text='Width')
        self.height_label = tk.Label(self.custom_size_frame, padx=20, text='Height')
        self.width_entry = tk.Entry(self.custom_size_frame, width=8)
        self.height_entry = tk.Entry(self.custom_size_frame, width=8)

        self.width_label.pack(side=tk.LEFT)
        self.width_entry.pack(side=tk.LEFT)
        self.height_label.pack(side=tk.LEFT)
        self.height_entry.pack(side=tk.LEFT)

        self.custom_size_frame.pack()

    def _initialize_save_load_config_frame(self) -> None:
        self.save_load_frame = tk.Frame(self)

        self.save_button = tk.Button(self.save_load_frame, padx=20, pady=10, text='Save', border=10)
        self.load_button = tk.Button(self.save_load_frame, padx=20, pady=10, text='Load', border=10)

        self.save_button.pack(side=tk.LEFT)
        self.load_button.pack(side=tk.LEFT)

        self.save_load_frame.pack()

        self.save_button.config(command=self.on_save)
        self.load_button.config(command=self.on_load)

    def _initialize_record_scene_frame(self) -> None:
        self.record_scene_frame = tk.Frame(self)

        self.record_scene_checkbox = tk.Checkbutton(self.record_scene_frame, text='Record Scene', variable=self._record_scene_var)
        
        self.record_scene_checkbox.pack(side=tk.LEFT)

        self.record_scene_frame.pack()

    def _initialize_replay_screen_frame(self) -> None:
        self.replay_scene_frame = tk.Frame(self)

        self.replay_scene_button = tk.Button(self.replay_scene_frame, padx=20, pady=10, text='Replay Scene...', border=10)

        self.replay_scene_button.pack(side=tk.LEFT)

        self.replay_scene_frame.pack()

        self.replay_scene_button.config(command=self.on_replay_scene)

    def on_apply(self) -> None:
        self.save_config(self.temp_config_path)
        self.master.destroy()

    def on_close(self) -> None:
        self.master.destroy()

    def on_load(self) -> None:
        self.config_path = filedialog.askopenfilename(initialdir=Configuration.CONFIGS_DIR,
                                                      title='Select a file',
                                                      filetypes=[('Configuration Files', '.yml')])
        self.load_config()

    def on_save(self) -> None:
        save_path = filedialog.asksaveasfilename(initialdir=Configuration.CONFIGS_DIR,
                                                 title='Save File',
                                                 filetypes=[('Configuration Files', '.yml')],
                                                 initialfile='my_config.yml')
        self.save_config(save_path)

    def on_replay_scene(self) -> None:
        scene_path = filedialog.askopenfilename(initialdir=Configuration.LOG_DIR,
                                                title='Open Recorded Scene',
                                                filetypes=[('Saved Recordings', '.json')])
        
        with open(scene_path, 'r') as f:
            self.config_dict = json.load(f)

        self.config_dict['record_scene'] = False
        self.load_config(replay=True)

        self.on_apply()

    def load_config(self, replay=False) -> None:
        if not replay:
            self.config_dict = self.configuration.parse_config(self.config_path)

        self.light_source_slider.set(self.config_dict['light_source'])

        self.width_entry.delete(0, tk.END)
        self.width_entry.insert(0, str(self.config_dict['width']))

        self.height_entry.delete(0, tk.END)
        self.height_entry.insert(0, str(self.config_dict['height']))

        if self.config_dict['record_scene']:
            self.record_scene_checkbox.select()
        else:
            self.record_scene_checkbox.deselect()

    def save_config(self, path) -> None:

        self.config_dict['light_source'] = int(self.light_source_slider.get())
        self.config_dict['width'] = int(self.width_entry.get())
        self.config_dict['height'] = int(self.height_entry.get())
        self.config_dict['record_scene'] = self._record_scene_var.get()

        self.configuration.write_config(self.config_dict, path)

    def get_window_size(self) -> str:
        return "{0}x{1}".format(self.width, self.height)
    
    def run(self) -> None:
        self.master.withdraw()
        self.master.mainloop()
