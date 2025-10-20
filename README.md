# PDF to Word Converter

A simple and user-friendly desktop application built with Python that converts PDF files to Word documents (DOCX format) with a graphical user interface.

## Features

- 🖱️ **Simple GUI Interface** - Easy-to-use graphical interface built with Tkinter
- 📄 **PDF to DOCX Conversion** - Convert entire PDF documents to editable Word files
- 🎯 **File Browser Integration** - Select PDF files using a native file dialog
- ✅ **Conversion Status** - Real-time feedback on conversion success or errors
- 🚀 **Fast Processing** - Efficient conversion using the pdf2docx library

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- pdf2docx library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MuhammadMagdy7/PDFtoWORD.git
   cd PDFtoWORD
   ```

2. **Install required dependencies:**
   ```bash
   pip install pdf2docx
   ```

   Note: `tkinter` is typically included with Python installations. If you encounter issues, you may need to install it separately:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **Fedora**: `sudo dnf install python3-tkinter`
   - **macOS**: Usually pre-installed with Python

## Usage

1. **Run the application:**
   ```bash
   python index.py
   ```

2. **Convert a PDF file:**
   - Click the "Select PDF" button to browse and select your PDF file
   - Alternatively, you can manually enter the PDF file path in the input field
   - Click the "Convert PDF to Word" button
   - The converted DOCX file will be saved in the same directory as the original PDF with the same filename

3. **Check the conversion status:**
   - Success messages will display the output file location
   - Error messages will help you troubleshoot any issues

## How It Works

The application uses the `pdf2docx` library to extract content from PDF files and convert them into editable Word documents. The conversion process:

1. Reads the PDF file structure
2. Extracts text, images, and formatting
3. Converts the content to DOCX format
4. Saves the output file with the same name as the input (with .docx extension)

## Example

```
Input:  document.pdf
Output: document.docx (saved in the same directory)
```

## Limitations

- Complex PDF layouts may not convert perfectly
- Some formatting elements might require manual adjustment in the output file
- The conversion quality depends on the complexity of the source PDF

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available for personal and educational use.

## Author

**Muhammad Magdy**
- GitHub: [@MuhammadMagdy7](https://github.com/MuhammadMagdy7)

## Acknowledgments

- Built with [pdf2docx](https://github.com/dothinking/pdf2docx) library
- GUI powered by Python's Tkinter library

---

⭐ If you find this project helpful, please consider giving it a star!
