# PDF to Word Converter

A simple and user-friendly desktop application to convert PDF files to Word documents (DOCX format) using Python and Tkinter.

## Features

- **Easy-to-use GUI**: Simple graphical interface built with Tkinter
- **Quick Conversion**: Convert PDF files to DOCX format with a single click
- **File Browser**: Built-in file selector to easily choose PDF files
- **Status Updates**: Real-time feedback on conversion progress and errors
- **Automatic Naming**: Output files are automatically named based on the input PDF

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)
- pdf2docx

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MuhammadMagdy7/PDFtoWORD.git
cd PDFtoWORD
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pdf2docx
```

**Note**: `tkinter` is typically included with Python installations. If you need to install it separately:
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On Fedora: `sudo dnf install python3-tkinter`
- On macOS: It should be pre-installed with Python

## Usage

1. Run the application:
```bash
python index.py
```

2. The application window will appear with the following options:
   - **Enter or select PDF path**: You can either type the path manually or use the "Select PDF" button
   - **Select PDF**: Click this button to browse and select a PDF file
   - **Convert PDF to Word**: Click this button to start the conversion

3. After conversion:
   - The DOCX file will be saved in the same directory as the source PDF
   - The output filename will be the same as the input, with a `.docx` extension
   - A status message will confirm successful conversion or display any errors

## Example

```
Input:  /path/to/document.pdf
Output: /path/to/document.docx
```

## How It Works

The application uses the `pdf2docx` library to parse PDF files and convert them to Word documents. The conversion process:
1. Reads the PDF file structure
2. Extracts text, images, and formatting
3. Creates a DOCX file with similar layout and content
4. Preserves as much of the original formatting as possible

## Limitations

- Complex PDF layouts may not convert perfectly
- Some advanced PDF features (like forms or annotations) may not be preserved
- Scanned PDFs (images) may not convert well without OCR

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Muhammad Magdy - [MuhammadMagdy7](https://github.com/MuhammadMagdy7)

## Acknowledgments

- Built with [pdf2docx](https://github.com/dothinking/pdf2docx) library
- GUI created using Python's Tkinter library
