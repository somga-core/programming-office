import tkinter as tk

def markdown_to_sheet(markdown, sheet):
    for symbol_index in range(len(markdown)):
        symbol = markdown[symbol_index]
        sheet.insert("end-1c", symbol)

def sheet_to_markdown(sheet):
    tag_symbols = {
        "italic": "*",
        "bold": "**",
        "overstrike": "~~",
        "code": "`"
    }

    end_index = sheet.index("end-1c")
    current_index = "1.0"
    result = ""
    tag_starts = {}
    tag_ends = {}

    for tag in sheet.tag_names():
        if tag != "sel":
            tag_ranges = sheet.tag_ranges(tag)
            for tag_range_index in range(len(tag_ranges)):
                if tag_range_index % 2 == 0:
                    tag_starts[str(tag_ranges[tag_range_index])] = tag
                else:
                    tag_ends[str(sheet.index(f"{tag_ranges[tag_range_index]}-1c"))] = tag  

    while current_index != end_index:
        next_index = str(sheet.index(f"{current_index}+1c"))

        symbol = sheet.get(current_index, next_index)

        if current_index in tag_starts:
            result += tag_symbols[tag_starts[current_index]]

        if symbol in tuple(tag_symbols.values()):
            result += "\\"

        result += symbol

        if current_index in tag_ends:
            result += tag_symbols[tag_ends[current_index]]
        
        current_index = str(sheet.index(next_index))

    return result