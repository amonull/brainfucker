import os
import sys
# sys.path.append(os.path.expanduser("~/.config/brainfucker/"))

import tkinter as tk
import tkinter.ttk as ttk

from .utils.text_frame import TextFrame
from .utils.menu import MainMenu

# try:
#     from keybinds import conf # try to import from /home/{user}/.config/noter/keybinds/conf.py
# except ImportError:
#     print("keybinds.conf not found in noter config dir. Using defualt keybinds")
#     from .keybinds import conf # import from {here}/keybinds/conf.py


class Editor(tk.Tk):
    def __init__(self, font: tuple):
        super().__init__()

        # styling
        self.font = font
        self.update_title()
        self.minsize(400, 300)
        # NOTE: use self.config(bg="<>") to set color

        # correct corner placement
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        text_frame = TextFrame(self, font, "black")

        # place objs
        self.config(menu=MainMenu(self, font))
        text_frame.pack(side="top", fill="both", expand=True)
    
    def update_title(self, new_name: str = "New File"):
        self.file_name = new_name
        self.title(f"Brainfucker - {self.file_name}")
