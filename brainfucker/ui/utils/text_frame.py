import tkinter as tk


from .colorizer import Colorize


class TextFrame(tk.Frame):
    def __init__(self, parent: tk.Tk, font: tuple, cursor_color: str = "black") -> None:
        super().__init__(parent)

        text_box = tk.Text(self, highlightthickness=0, padx=5, pady=5, wrap="none", font=font, insertbackground=cursor_color)
        y_scrollbar = tk.Scrollbar(self, command=text_box.yview, orient=tk.VERTICAL)
        x_scrollbar = tk.Scrollbar(self, command=text_box.xview, orient=tk.HORIZONTAL)
        text_box.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        text_box.focus_set()

        # Colorizer
        colorize = Colorize(text_box)
        text_box.bind("<KeyRelease>", colorize.find_pattern)
        colorize.find_pattern() # colorizes when file opened

        # place in frame
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar.pack(side="bottom", fill="x")
        text_box.pack(side="left", fill="both", expand=True)

        # expose tk.Text to tk.Frame
        self.insert = text_box.insert
        self.delete = text_box.delete
        self.mark_set = text_box.mark_set
        self.get = text_box.get
        self.index = text_box.index
        self.search = text_box.search
