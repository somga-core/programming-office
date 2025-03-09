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
        self.title(TITLE)
        self.iconbitmap("")

        # Widgets
        self.top_bar = TopBar(self)
        self.sheet = Sheet(self)
        self.tooltip_label = tk.Label(self, text="", bg="lightyellow", relief="solid", borderwidth=1)

        self.top_bar_buttons = []

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "⎙", function=self.sheet.load_file, tooltip="Open file"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "⎗", function=self.sheet.save_file, tooltip="Save file"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "⎘", function=self.sheet.save_as_file, tooltip="Save file as"))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "R", tag="reset", tooltip="Reset style"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "𝘐", tag="italic", tooltip="Make italic text"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "𝗕", tag="bold", tooltip="Make bold text"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "S̶", tag="overstrike", tooltip="Make overstrike text"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "🖵", tag="code", tooltip="Make code text"))
        
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label, ""))

        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "𝗧", function=self.sheet.insert_title, tooltip="Create title"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "🖾", function=self.sheet.insert_image, tooltip="Create image"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "🖈", function=self.sheet.insert_link, tooltip="Create link"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "©", function=self.sheet.insert_quote, tooltip="Create quote"))
        self.top_bar_buttons.append(TopBarButton(self.top_bar, self.sheet, self.tooltip_label,
            "🖃", function=self.sheet.insert_code, tooltip="Create code box"))

if __name__ == "__main__":
    window = MainWindow()
    window.sheet.load_file()
    window.mainloop()