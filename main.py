import tkinter as tk
from settings import *
from time import sleep

class MainWindow(tk.Tk):
    def __init__(self):
        # Tk settings
        super().__init__()
        self.geometry("1600x900")
        self.config(background=BG_COLOR)
        self.title("Programming office")

        # Variables
        self.file_name = FILE_NAME

        # Elements
        self.top_bar = tk.Label(
            self,
            background=INTERFACE_COLOR,
            highlightthickness=True,
            highlightbackground=OUTLINE_COLOR
        )
        self.top_bar.pack(side="top", ipady=BAR_WIDTH//2, fill="x")

        self.sheet = tk.Text(
            self,
            background=BG_COLOR,
            borderwidth=0,
            relief="flat",
            foreground=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            highlightthickness=False
        )
        self.sheet.pack(side="left", fill="both", padx=TEXT_PADDING, pady=TEXT_PADDING)
        
        self.scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.sheet.yview
        )
        self.scrollbar.pack(side="right", fill="y")

        # Binds

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()