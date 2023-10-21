import tkinter as tk

class BrainfuckDebugger(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()

    # TODO: make sure to colorize this as well
    
    # How it should look

    # First half txtbox holding the file and a cursor that colors each char it is currently passing
    # second half zoomed in cells with their current values
    # box on bottom right output terminal
