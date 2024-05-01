import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert_pdf_to_docx():
    """Converts a selected PDF file to a Word document (DOCX)."""

    # Get PDF file path
    pdf_file = pdf_path_entry.get()

    if pdf_file:
        try:
            # Create output filename with same name and .docx extension
            docx_file = pdf_file.replace(".pdf", ".docx")

            # Convert PDF to DOCX using pdf2docx
            cv = Converter(pdf_file)
            cv.convert(docx_file, start=0, end=None)  # Convert entire PDF

            # Success message
            message_label.config(text="PDF converted successfully to " + docx_file)
        except Exception as e:
            # Error handling
            message_label.config(text="Error converting PDF: " + str(e))
    else:
        message_label.config(text="Please select a PDF file.")

# Create the main window
root = tk.Tk()
root.title("PDF to Word Converter")

# Input field for PDF path
pdf_path_label = tk.Label(root, text="Enter or select PDF path:")
pdf_path_label.grid(row=0, column=0)
pdf_path_entry = tk.Entry(root)
pdf_path_entry.grid(row=0, column=1)

# Button to select and convert PDF
select_button = tk.Button(root, text="Select PDF", command=lambda: pdf_path_entry.insert(tk.END, filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("Portable Document Format", "*.pdf")]
    )))
select_button.grid(row=0, column=2)

convert_button = tk.Button(root, text="Convert PDF to Word", command=convert_pdf_to_docx)
convert_button.grid(row=1, columnspan=3)

# Label to display conversion status
message_label = tk.Label(root, text="")
message_label.grid(row=2, columnspan=3)

# Run the main loop
root.mainloop()
