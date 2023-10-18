from dataclasses import dataclass, astuple, field


@dataclass
class Font:
    """
    holds values needed for fonts in tkinter

    default values still nececry as calls to only Font() are still
    made if [Font] is non existent in config.ini
    and Font() is still used in Config()

    font types = 
        1       = system font
        tuple   = user set settings (tuple)

    font tuple  = (name, size, style, slant, underline, overstrike)
    style =
        normal
        bold
    slant =
        roman (normal)
        italic
    underline = 
        normal
        underline
    overstrike =
        normal
        overstrike
    """
    family:     str = "Font" # should use default font in tkinter
    size:       int = 0
    bold:       str = "normal"
    italic:     str = "normal"
    underline:  str = "normal"
    overstrike: str = "normal"


@dataclass
class Config:
    font_class: Font    = field(default_factory=Font)
    theme:      str     = "default"

    def __post_init__(self) -> None:
        """
        create font tuple
        """
        self.font = astuple(self.font_class)
