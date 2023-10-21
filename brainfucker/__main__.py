from .ui.editor import Editor
from .utils.config.reader import ReadConfig


def main():
    config = ReadConfig().return_values()

    # APP
    app = Editor(config.font)
    app.mainloop()

if __name__ == "__main__":
    main()
