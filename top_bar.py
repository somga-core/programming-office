from settings import *
import tkinter as tk

class TopBar(tk.Label):
    def __init__(self, master):
        super().__init__(master)

        # Settings
        self.configure(
            background=INTERFACE_COLOR,
            highlightthickness=OUTLINE_WIDTH,
            highlightbackground=OUTLINE_COLOR
        )

        # Placing
        self.pack(side="top", fill="x")