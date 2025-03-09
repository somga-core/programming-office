from settings import *
import tkinter as tk
from urllib.request import urlopen

class EditDialog(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        # Settings
        self.title("Configure")
        self.configure(
            background=INTERFACE_COLOR
        )
        self.geometry(f"{EDIT_DIALOG_WIDTH}x{EDIT_DIALOG_HEIGHT}")
        self.iconbitmap("")

        # Variables
        self.parent = parent

        # Widgets
        self.entries = []
        for parameter in parent.parameters:
            tk.Label(
                self,
                background=INTERFACE_COLOR,
                border=0,
                highlightthickness=0,
                foreground=TEXT_COLOR,
                font=(FONT, BUTTONS_FONT_SIZE),
                text=parameter,
                anchor="w"
            ).pack(padx=BUTTONS_PADDING, fill="x")

            if parameter in parent.long_parameters:
                self.entries.append(tk.Text(
                    self,
                    background=BG_COLOR,
                    border=0,
                    highlightthickness=OUTLINE_WIDTH,
                    highlightcolor=OUTLINE_COLOR,
                    highlightbackground=OUTLINE_COLOR,
                    foreground=TEXT_COLOR,
                    insertbackground=TEXT_COLOR,
                    font=(FONT, BUTTONS_FONT_SIZE),
                    height=5
                )) 
                self.entries[-1].insert(1.0, parent.parameters[parameter])
            else:
                self.entries.append(tk.Entry(
                    self,
                    background=BG_COLOR,
                    border=0,
                    highlightthickness=OUTLINE_WIDTH,
                    highlightcolor=OUTLINE_COLOR,
                    highlightbackground=OUTLINE_COLOR,
                    foreground=TEXT_COLOR,
                    insertbackground=TEXT_COLOR,
                    font=(FONT, BUTTONS_FONT_SIZE)
                ))
                self.entries[-1].insert(0, parent.parameters[parameter])
            self.entries[-1].pack(padx=BUTTONS_PADDING, pady=BUTTONS_PADDING, fill="x")

        self.submit_button = tk.Button(
                self,
                background=INTERFACE_COLOR,
                border=0,
                highlightthickness=OUTLINE_WIDTH,
                highlightcolor=OUTLINE_COLOR,
                highlightbackground=OUTLINE_COLOR,
                foreground=TEXT_COLOR,
                activebackground=OUTLINE_COLOR,
                activeforeground=TEXT_COLOR,
                font=(FONT, BUTTONS_FONT_SIZE),
                text="Submit"
        )
        self.submit_button.pack(side="right", anchor="ne", padx=BUTTONS_PADDING, pady=BUTTONS_PADDING)

        # Binds
        self.submit_button.bind("<ButtonPress-1>", self.submit)

    def submit(self, event):
        for parameter in self.parent.parameters:
            result = self.entries[list(self.parent.parameters.keys()).index(parameter)]
            if not parameter in self.parent.long_parameters:
                result = result.get()
            else:
                result = result.get(1.0, "end")
            self.parent.parameters[parameter] = result

        self.parent.update()
        self.destroy()

class SheetInserted(tk.Button):
    def __init__(self, sheet, parameters_names, default_parameters, long_parameters):
        super().__init__(sheet)

        # Settings
        self.configure(
            background=BG_COLOR,
            foreground=TEXT_COLOR,
            font=(FONT, SHEET_FONT_SIZE),
            text="test",
            highlightthickness=OUTLINE_WIDTH,
            highlightbackground=INTERFACE_COLOR,
            highlightcolor=INTERFACE_COLOR,
            border=0,
            activebackground=BG_COLOR,
            activeforeground=TEXT_COLOR,
            justify="left"
        )

        # Variables
        self.parameters = dict(zip(parameters_names.copy(), default_parameters.copy()))
        self.long_parameters = long_parameters
        self.sheet = sheet

        # Binds
        self.bind("<ButtonPress-1>", self.edit_parameters)

        self.create()
        self.update()

    def edit_parameters(self, event=None):
        try:
            self.dialog.destroy()
        except:
            pass

        self.dialog = EditDialog(self)

        self.dialog.mainloop()

    def create(self):
        self.sheet.window_create("insert", window=self)
        self.sheet.update_text()
        self.sheet.update_text()

    def update(self):
        pass

class SheetTitle(SheetInserted):
    def __init__(self, sheet):
        super().__init__(sheet, ["Title", "Size (1 - 6)"], ["Title", "1"], [])

    def update(self):
        if not self.parameters["Size (1 - 6)"] in ["1", "2", "3", "4", "5", "6"]:
            self.parameters["Size (1 - 6)"] = "1"
        font_size = int(SHEET_FONT_SIZE * 0.5 * (6 - int(self.parameters["Size (1 - 6)"])))
        self.configure(
            text=self.parameters["Title"],
            font=(FONT, font_size),
        )

class SheetCode(SheetInserted):
    def __init__(self, sheet):
        super().__init__(sheet, ["Language", "Code"], ["python", "print('Hello world!')"], ["Code"])
        self.configure(
            font=(CODE_FONT, SHEET_FONT_SIZE)
        )

        self.language = ""

    def update(self):
        self.language = self.parameters["Language"]
        self.configure(
            text=self.parameters["Code"].strip("\n")
        )

class SheetQuote(SheetInserted):
    def __init__(self, sheet):
        super().__init__(sheet, ["Quote"], ["Quote"], ["Quote"])

    def update(self):
        self.configure(
            text='«' + self.parameters["Quote"].strip("\n") + '»'
        )

class SheetImage(SheetInserted):
    def __init__(self, sheet):
        super().__init__(sheet, ["Alt text", "Link", "Tooltip"],
            ["Alt text", "https://www.python.org/static/img/python-logo.png", "Python logo"], [])
        
        self.alt_text = ""
        self.tooltip_text = ""

    def update(self):
        # Load image from url
        image_byt = urlopen(self.parameters["Link"]).read()
        self.image = tk.PhotoImage(data=image_byt)

        self.alt_text = self.parameters["Alt text"]
        self.tooltip_text = self.parameters["Tooltip"]
        self.configure(
            image=self.image
        )

class SheetLink(SheetInserted):
    def __init__(self, sheet):
        super().__init__(sheet, ["Text", "Link", "Tooltip"],
            ["Link", "https://www.python.org/", "Python site"], ["Quote"])
        self.configure(
            highlightthickness=0,
            font=(FONT, SHEET_FONT_SIZE, "underline")
        )

        self.link = ""
        self.tooltip_text = ""

    def update(self):
        self.link = self.parameters["Link"]
        self.tooltip_text = self.parameters["Tooltip"]
        self.configure(
            text=self.parameters["Text"].strip("\n")
        )