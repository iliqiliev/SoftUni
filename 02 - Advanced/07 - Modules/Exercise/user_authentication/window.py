#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

import sv_ttk
import darkdetect


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "welcome.ui"


class UAGui:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        # Main widget
        self.mainwindow: tk.Toplevel = builder.get_object("home_screen", master)
        builder.connect_callbacks(self)

        self.set_theme()

    def run(self):
        self.mainwindow.mainloop()

    def register(self):
        pass

    def login(self):
        pass

    def home(self):
        pass

    def set_theme(self) -> None:
        system_theme = darkdetect.theme().lower()
        sv_ttk.set_theme(system_theme)
