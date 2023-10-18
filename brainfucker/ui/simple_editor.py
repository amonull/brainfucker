import tkinter as tk
import tkinter.ttk as ttk


class SimpleEditor(tk.Tk):
    # def __init__(self, font: tuple, theme: str) -> None:
    def __init__(self) -> None:
        super().__init__()

        # GUI settings
        # self.font = font
        # self.style = ttk.Style()
        # self.style.theme_use(theme)

        # editor settings
        self.file_name = "New File" # if not file_path else Path(file_path).name
        self.title(f"brainfucker - {self.file_name}")
        self.minsize(400, 300)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # text box
        _cursor_color = "white"#"black" if appearance != "Dark" else "white"
        self.txt_box = tk.Text(self, highlightthickness=0, padx=5, pady=5, wrap="none", insertbackground=_cursor_color)
        self.txt_box.focus_set()

        # scrollbar vertical
        y_scrollbar = tk.Scrollbar(self, command=self.txt_box.yview, orient=tk.VERTICAL)
        # scrollbar horizontal
        x_scrollbar = tk.Scrollbar(self, command=self.txt_box.xview, orient=tk.HORIZONTAL)

        self.txt_box.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        # place objs
        self.txt_box.grid(row=0, column=0, sticky="nsew")
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        x_scrollbar.grid(row=1, column=0, sticky="we")

        # self.config(menu=self.menu())

editor = SimpleEditor()
editor.mainloop()
