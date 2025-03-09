from settings import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
from convertor import *
from sheet_inserted import *

with open("settings.py") as settings_file:
    exec(settings_file.read())
    
class Sheet(tk.Text):
    def __init__(self, master):
        super().__init__(master)

        # Settings
        self.configure(
            background=BG_COLOR,
            border=0,
            foreground=TEXT_COLOR,
            selectbackground=INTERFACE_COLOR,
            selectforeground=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            highlightthickness=False,
            font=(FONT, SHEET_FONT_SIZE)
        )
        self.file_name = DEFAULT_NAME

        # Placing
        self.pack(side="left", fill="both", padx=TEXT_PADDING, pady=TEXT_PADDING)

        # Binds
        self.bind("<Control-a>", self.select_all)
        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-S>", self.save_as_file)
        self.bind("<Control-o>", self.load_file)
        self.bind("<KeyRelease>", self.update_text)

        # Tags configuring
        self.tag_configure("italic", font=(FONT, SHEET_FONT_SIZE, "italic"), background=INTERFACE_COLOR)
        self.tag_configure("bold", font=(FONT, SHEET_FONT_SIZE, "bold"))
        self.tag_configure("overstrike", font=(FONT, SHEET_FONT_SIZE, "overstrike"), background=INTERFACE_COLOR)

        self.tag_configure("title-6", font=(FONT, int(SHEET_FONT_SIZE//2), "bold"))
        self.tag_configure("title-5", font=(FONT, int(SHEET_FONT_SIZE//1.5), "bold"))
        self.tag_configure("title-4", font=(FONT, int(SHEET_FONT_SIZE), "bold"))
        self.tag_configure("title-3", font=(FONT, int(SHEET_FONT_SIZE*1.5), "bold"))
        self.tag_configure("title-2", font=(FONT, int(SHEET_FONT_SIZE*2), "bold"))
        self.tag_configure("title-1", font=(FONT, int(SHEET_FONT_SIZE*2.5), "bold"))

        self.tag_configure("code", font=(CODE_FONT, SHEET_FONT_SIZE),
            background=INTERFACE_COLOR, selectforeground=TEXT_COLOR, selectbackground=OUTLINE_COLOR)
        self.tag_configure("quote", font=(FONT, int(SHEET_FONT_SIZE*2.5)))

    def select_all(self, event):
        self.tag_add(tk.SEL, '1.0', "end")
        return 'break'
    
    def load_file(self, event=None):
        self.file_name = askopenfilename(filetypes=FILE_TYPES, initialdir="./")
        if not self.file_name:
            self.file_name = DEFAULT_NAME
        with open(self.file_name) as file:
            self.delete(1.0, "end")
            markdown_to_sheet(file.read(), self)
        file_name_pathless = self.file_name.split("/")[-1]
        self.master.title(f"{TITLE} - {file_name_pathless}")
    
    def save_as_file(self, event=None):
        self.file_name = asksaveasfilename(filetypes=FILE_TYPES, initialdir="./")
        with open(self.file_name, "w") as file:
            file.write(sheet_to_markdown(self))

    def save_file(self, event=None):
        with open(self.file_name, "w") as file:
            file.write(sheet_to_markdown(self))

    def insert_title(self, event):
        SheetTitle(self)

    def insert_image(self, event):
        SheetImage(self)

    def insert_link(self, event):
        SheetLink(self)

    def insert_code(self, event):
        SheetCode(self)

    def insert_quote(self, event):
        SheetQuote(self)

    def update_text(self, event=None):
        for window_name in self.window_names():
            if not "sheetlink" in window_name and not "sheetimage" in window_name:
                index = self.index(window_name)
                if self.index(f"{index}+1c") != self.index(f"{index} lineend"):
                    self.insert(f"{index}+1c", "\n")
                if str(index).split(".")[1] != "0":
                    self.insert(index, "\n")