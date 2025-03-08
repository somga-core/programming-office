from settings import *
import tkinter as tk

class TopBarButton(tk.Button):
    index = -1

    def __init__(self, master, sheet, text, tag=None, function=None):
        super().__init__(master)

        # Variables
        self.sheet = sheet
        self.tag = tag
        self.function = function
        
        # Settings
        self.configure(
            background=INTERFACE_COLOR,
            highlightthickness=OUTLINE_WIDTH,
            highlightbackground=OUTLINE_COLOR,
            border=0,
            text=text,
            activebackground=OUTLINE_COLOR,
            foreground=TEXT_COLOR,
            activeforeground=TEXT_COLOR,
            font=(FONT, BUTTONS_FONT_SIZE)
        )
        if not text:
            self.configure(
                highlightthickness=0,
                activebackground=INTERFACE_COLOR,
            )

        # Placing
        self.grid(row=0, column=self.conut_index(),
            padx=BUTTONS_PADDING, pady=BUTTONS_PADDING)

        # Binds
        if not tag is None and not function is None:
            pass
        elif tag is None:
            self.bind("<ButtonPress-1>", self.function)
        elif function is None:
            self.bind("<ButtonPress-1>", self.change_text)

    def clear_selection_tags(self, tags):
        for tag in tags:
            if tag != 'sel':
                self.sheet.tag_remove(tag, "sel.first", "sel.last")

    def change_text(self, event):
        if self.tag in ("reset", "title-1", "title-2", "title-3", "title-4", "title-5", "title-6"):
            self.clear_selection_tags(self.sheet.tag_names())

        if self.tag in ("quote", "code"):
            self.clear_selection_tags(("bold", "italic", "overstrike"))

        if self.tag in ("bold", "italic", "overstrike"):
            self.clear_selection_tags(("quote", "code"))

        if self.tag != "reset":
            self.sheet.tag_add(self.tag, "sel.first", "sel.last")

    @staticmethod
    def conut_index():
        TopBarButton.index += 1
        return TopBarButton.index