import tkinter as tk
import re

class Colorize:
    def __init__(self,
                 text_box: tk.Text,
                 comments: str = "#808080",
                 changePtrVal: str = "#068e00",
                 changePtr: str = "#e7ff28",
                 printPtr: str = "#00fcf6",
                 getValPtr: str = "#0028fc",
                 brackets: str = "#b30000") -> None:

        self.patterns: list[list] = [
                                    ["(\+|-)", changePtrVal],
                                    ["(<|>)", changePtr],
                                    ["\.", printPtr],
                                    [",", getValPtr],
                                    ["(\[|\])", brackets],
                                    ["[^\[\]\+-\.,><]", comments] # ignore all operators
                                    ]
        self.text_box = text_box

    def find_pattern(self, event=None):
        for tag in self.text_box.tag_names():
            self.text_box.tag_remove(tag, "1.0", "end")
        i = 0
        for pattern, color in self.patterns:
            for start, end in self.search_re(pattern, self.text_box.get('1.0', tk.END)):
                self.text_box.tag_add(f'{i}', start, end)
                self.text_box.tag_config(f'{i}', foreground=color)

                i+=1

    def search_re(self, pattern, text):
        matches = []

        text = text.splitlines()
        for i, line in enumerate(text):
            for match in re.finditer(pattern, line):

                matches.append(
                    (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
                )
        return matches
