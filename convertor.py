import tkinter as tk

def markdown_to_sheet(markdown, sheet):
    sheet.insert(1.0, markdown)

def sheet_to_markdown(sheet):
    result = sheet.get(1.0, "end")

    return result