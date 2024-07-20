# PDF to Excel Converter in Python

```bash
python pdf_to_excel.py
```

## Usage

```shell
python pdf_to_excel.py 'path_to_pdf_file.pdf' 'path_to_excel_file.xlsx'
```

or to convert all pdf files in the folder to excel files

```shell
python pdf_to_excel.py
```

Replace `path_to_pdf_file.pdf` with the path to the PDF file you want to convert, and replace `path_to_excel_file.xlsx` with the path where you want to save the Excel file.

## Dependencies

- `tabula-py`: A simple wrapper for Tabula, which can read tables in a PDF.
- `pandas`: A powerful data manipulation library.
- `openpyxl`: A library to read and write Excel files.

You can install these dependencies with pip:

```bash
pip3 install tabula-py pandas openpyxl
```

## Based on:
https://github.com/LadyKerr/pdf-to-excel

## Features:
1. Converts all pdf files in the folder to excel files
2. Merges all tables with same column names

## Works with: 
1. Federal Bank PDF account statements(Last checked: 20 July 2024)

## TODO:
1. Make GUI version