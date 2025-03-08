import tkinter as tk
from settings import *
from top_bar import *
from top_bar_button import *
from sheet import *

with open("settings.py") as settings_file:
    exec(settings_file.read())

class MainWindow(tk.Tk):
    def __init__(self):
        # Tk settings
        super().__init__()
        self.geometry("1600x900")
        self.config(background=BG_COLOR)
        self.title("Programming office")

        # Widgets
        self.top_bar = TopBar(self)
        self.sheet = Sheet(self)

        self.top_bar_buttons = []

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "🗀", function=self.sheet.load_file))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "⎘", function=self.sheet.save_file))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, ""))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "R", tag="reset"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "𝘐", tag="italic"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "𝗕", tag="bold"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "U̲", tag="underline"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "S̶", tag="overstrike"))
        
        self.sheet.load_file()

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()