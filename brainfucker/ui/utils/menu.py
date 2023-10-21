import tkinter as tk


class SubMenuFiles(tk.Menu):
    def __init__(self, parent: tk.Menu, font: tuple) -> None:
        super().__init__(parent, tearoff=0, font=font)

        self.add_command(label="New", command=self.new_file)
        self.add_command(label="Open", command=self.open_file)
        self.add_command(label="Save", command=self.save_file)
        self.add_command(label="Save as...", command=self.save_file_as)

    def new_file(self) -> None:
        pass

    def open_file(self) -> None:
        pass

    def save_file(self) -> None:
        pass

    def save_file_as(self) -> None:
        pass


class MainMenu(tk.Menu):
    def __init__(self, parent: tk.Tk, font: tuple) -> None:
        super().__init__(parent, font=font)

        self.add_cascade(label="File", menu=SubMenuFiles(self, font))
        self.add_command(label="About", command=lambda: print("got here"))
