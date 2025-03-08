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
            "🗁", function=self.sheet.load_file))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "🗎", function=self.sheet.save_file))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "R", tag="reset"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "𝘐", tag="italic"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "𝗕", tag="bold"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "S̶", tag="overstrike"))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T1", tag="title-1"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T2", tag="title-2"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T3", tag="title-3"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T4", tag="title-4"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T5", tag="title-5"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "T6", tag="title-6"))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "🖵", tag="code"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "©", tag="quote"))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "🖾", function=self.sheet.insert_image))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet,
            "🖈", function=self.sheet.insert_link))

if __name__ == "__main__":
    window = MainWindow()
    window.sheet.load_file()
    window.mainloop()