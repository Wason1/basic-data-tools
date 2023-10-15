import openpyxl
import tkinter as tk
from tkinter import filedialog, simpledialog

def merge_similar_cells(filepath, column):
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active

    prev_value = None
    start_row = None

    max_row = ws.max_row
    for row in range(1, max_row + 1):
        current_value = ws[f"{column}{row}"].value

        if current_value == prev_value:
            if not start_row:
                start_row = row - 1
        else:
            if start_row:
                ws.merge_cells(start_row=start_row, start_col=ord(column) - 65, 
                               end_row=row-1, end_col=ord(column) - 65)
                start_row = None

        prev_value = current_value

    wb.save(filepath)

def main():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx")])
    if not filepath:
        return

    column = simpledialog.askstring("Input", "Enter the column (e.g. 'A'):")

    if column:
        merge_similar_cells(filepath, column.upper())
        tk.messagebox.showinfo("Success", "Cells merged successfully!")

if __name__ == "__main__":
    main()
