import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_and_save_txt():
    # Ask the user for the input .txt file
    txt_filepath = filedialog.askopenfilename(title="Select TXT File", filetypes=[("TXT files", "*.txt")])
    if not txt_filepath:
        return

    # Ask the user where to save the .xlsx file
    xlsx_filepath = filedialog.asksaveasfilename(title="Save XLSX File", filetypes=[("Excel files", "*.xlsx")], defaultextension=".xlsx")
    if not xlsx_filepath:
        return

    chunk_size = 50000  # Adjust this based on the average row size of your data and available memory
    first_chunk = True

    # Create a new Excel writer object
    with pd.ExcelWriter(xlsx_filepath, engine='openpyxl') as writer:
        for chunk in pd.read_csv(txt_filepath, delim_whitespace=True, chunksize=chunk_size):
            if first_chunk:
                # Write the header and data for the first chunk
                chunk.to_excel(writer, index=False, sheet_name='Sheet1', startrow=0)
                writer.sheets['Sheet1'].sheet_state = 'visible'
                first_chunk = False
            else:
                # Skip the header and write data for subsequent chunks
                chunk.to_excel(writer, index=False, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, header=False)

    messagebox.showinfo("Success", f"File saved successfully to {xlsx_filepath}")

def main():
    root = tk.Tk()
    root.title("TXT to XLSX Converter")

    # Create a button to initiate the file conversion
