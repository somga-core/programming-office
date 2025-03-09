import tkinter as tk

def markdown_to_sheet(markdown, sheet):
    # buffer = ""
    for symbol_index in range(len(markdown)):
        symbol = markdown[symbol_index]
        # prev_symbol = markdown[symbol_index - 1] if symbol_index > 0 else ""
        # next_symbol = markdown[symbol_index + 1] if symbol_index < len(markdown)-1 else ""

        # # Inserting symbol
        # for tag in sheet.tag_names():
        #     if tag != 'sel':
        #         sheet.tag_remove(tag, "end-1c", "end+1c")
        sheet.insert("end-1c", symbol)

        # Setting buffer
        # if "D" in buffer:
        #     for tag in sheet.tag_names():
        #         if tag != 'sel':
        #             sheet.tag_remove(tag, "end-3c", "end")
        #     buffer = buffer.replace("D", "")

        # if not "/" in buffer:
        #     if "d" in buffer:
        #         sheet.delete("end-2c", "end-1c")
        #         buffer = buffer.replace("d", "")
        #     else:
        #         if symbol == "*" or symbol == "_":
        #             if not "i" in buffer:
        #                 buffer += "i"
        #                 buffer += "D"
        #             else:
        #                 buffer = buffer.replace("i", "")
        #             sheet.delete("end-2c", "end-1c")

        #     if (symbol == next_symbol == "*" or symbol == next_symbol == "_"):
        #         if not "b" in buffer:
        #             buffer += "b"
        #             buffer += "D"
        #         else:
        #             buffer = buffer.replace("b", "")
        #         buffer += "d"

        #     if symbol == "`" or symbol == "`":
        #         if not "c" in buffer:
        #             buffer += "c"
        #             buffer += "D"
        #         else:
        #             buffer = buffer.replace("c", "")
        #         sheet.delete("end-2c", "end-1c")
        # else:
        #     buffer = buffer.replace("/", "")
        #     print(buffer)
        
        # if symbol == "\\":
        #     buffer += "/"
        #     sheet.delete("end-2c", "end-1c")

        # # Setting style
        # if "b" in buffer:
        #     sheet.tag_add("bold", "end-2c")
        # if "i" in buffer:
        #     sheet.tag_add("italic", "end-2c")
        # if "c" in buffer:
        #     sheet.tag_add("code", "end-2c")

def sheet_to_markdown(sheet):
    result = sheet.get(1.0, "end")

    return result