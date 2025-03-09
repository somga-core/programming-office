from settings import *
import tkinter as tk

with open("settings.py") as settings_file:
    exec(settings_file.read())

class TopBarButton(tk.Button):
    index = -1

    def __init__(self, master, sheet, tooltip_label, text, tag=None, function=None, tooltip=None):
        super().__init__(master)

        # Variables
        self.sheet = sheet
        self.tag = tag
        self.function = function
        self.tooltip_label = tooltip_label
        self.tooltip = tooltip
        
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

        if not self.tooltip is None:
            self.bind("<Enter>", self.show_tooltip)
            self.bind("<Leave>", self.hide_tooltip)

    def clear_selection_tags(self, tags):
        for tag in tags:
            if tag != 'sel':
                try:
                    self.sheet.tag_remove(tag, "sel.first", "sel.last")
                except tk.TclError:
                    pass

    def change_text(self, event):
        self.clear_selection_tags(self.sheet.tag_names())

        if self.tag != "reset":
            try:
                self.sheet.tag_add(self.tag, "sel.first", "sel.last")
            except tk.TclError:
                pass

        if "title" in self.tag:
            if self.sheet.index("sel.first").split(".")[1] != "0":
                self.sheet.insert("sel.first", "\n")

            if self.sheet.index("sel.last") != self.sheet.index("sel.last lineend"):
                self.sheet.insert("sel.last", "\n")

    def show_tooltip(self, event):
        self.tooltip_label.config(text=self.tooltip)
        self.tooltip_label.place(x=event.x_root + 10, y=event.y_root - 40)

    def hide_tooltip(self, event):
        self.tooltip_label.place_forget()

    @staticmethod
    def conut_index():
        TopBarButton.index += 1
        return TopBarButton.index