from settings import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk

class Sheet(tk.Text):
    def __init__(self, master):
        super().__init__(master)

        # Settings
        self.configure(
            background=BG_COLOR,
            borderwidth=0,
            relief="flat",
            foreground=TEXT_COLOR,
            selectbackground=INTERFACE_COLOR,
            selectforeground=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            highlightthickness=False,
            font=(FONT, SHEET_FONT_SIZE)
        )
        self.file_name = FILE_NAME

        # Placing
        self.pack(side="left", fill="both", padx=TEXT_PADDING, pady=TEXT_PADDING)

        # Binds
        self.bind("<Control-a>", self.select_all)
        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-o>", self.load_file)

        # Tags configuring
        self.tag_configure("italic", font=(FONT, SHEET_FONT_SIZE, "italic"))
        self.tag_configure("bold", font=(FONT, SHEET_FONT_SIZE, "bold"))
        self.tag_configure("overstrike", font=(FONT, SHEET_FONT_SIZE, "overstrike"))

        self.tag_configure("title-6", font=(FONT, int(SHEET_FONT_SIZE//2), "bold"))
        self.tag_configure("title-5", font=(FONT, int(SHEET_FONT_SIZE//1.5), "bold"))
        self.tag_configure("title-4", font=(FONT, int(SHEET_FONT_SIZE), "bold"))
        self.tag_configure("title-3", font=(FONT, int(SHEET_FONT_SIZE*1.5), "bold"))
        self.tag_configure("title-2", font=(FONT, int(SHEET_FONT_SIZE*2), "bold"))
        self.tag_configure("title-1", font=(FONT, int(SHEET_FONT_SIZE*2.5), "bold"))

        self.tag_configure("code", font=(CODE_FONT, SHEET_FONT_SIZE),
            background=INTERFACE_COLOR, selectforeground=INTERFACE_COLOR, selectbackground=TEXT_COLOR)
        self.tag_configure("quote", font=(FONT, int(SHEET_FONT_SIZE*2.5)))

    def select_all(self, event):
        self.tag_add(tk.SEL, '1.0', "end")
        return 'break'
    
    def load_file(self, event=None):
        self.file_name = askopenfilename(filetypes=FILE_TYPES, initialdir="./")
        if not self.file_name:
            quit()
        with open(self.file_name) as file:
            self.delete(1.0, "end")
            self.insert(1.0, file.read())

    def save_file(self, event=None):
        with open(self.file_name, "w") as file:
            file.write(self.get(1.0, "end"))

    def insert_image(self):
        pass

    def insert_link(self):
        pass