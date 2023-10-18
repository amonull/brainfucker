import os
import configparser

from .dataclasses import Font, Config


class ReadConfig:
    def __init__(self, path: str=os.path.expanduser("~/.config/brainfucker/config.ini")) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def read_font(self) -> Font:
        """
        creates and returns a font class using user settings

        does error checking to see if all keys being searched for are present if not default values are passed
        """
        font_section = self.config["Font"]

        _bold = "normal" if not font_section.getboolean("bold", fallback=False) else "bold"
        _italic = "normal" if not font_section.getboolean("italic", fallback=False) else "italic"
        _underline = "normal" if not font_section.getboolean("underline", fallback=False) else "underline"
        _overstrike = "normal" if not font_section.getboolean("overstrike", fallback=False) else "overstrike"

        return Font(
                family=font_section["family"] if "family" in font_section else "Font",
                size=font_section.getint("size", fallback=12),
                bold=_bold,
                italic=_italic,
                underline=_underline,
                overstrike=_overstrike,
                )

    def read_defaults(self):
        """
        incomplete
        more keys might be needed inside Defaults
        """
        defaults_section = self.config["Defaults"]

        return defaults_section["theme"] if "theme" in defaults_section else "default"

    def read_colors(self):
        pass

    def return_values(self) -> Config:
        """
        checks if sections exist if they do custmized values are collected and fed to Config()
        """
        _font = self.read_font() if "Font" in self.config.sections() else Font()
        _theme = self.read_defaults() if "Defaults" in self.config.sections() else "default"

        return Config(
                _font,
                _theme,
                )
