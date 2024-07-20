import tabula
import pandas as pd
import sys
import os

def pdf_to_excel(pdf_file_path, excel_file_path):
    # check if the pdf file path is valid
    if not os.path.exists(pdf_file_path):
        print(f"Error: {pdf_file_path} does not exist.")
        return
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages='all')

    # Merge all tables with the same columns
    merged_tables = {}
    for table in tables:
        columns_tuple = tuple(table.columns)
        if columns_tuple not in merged_tables:
            merged_tables[columns_tuple] = table
        else:
            merged_tables[columns_tuple] = pd.concat([merged_tables[columns_tuple], table], ignore_index=True)

    # Write each merged table to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for i, (columns, merged_table) in enumerate(merged_tables.items()):
            merged_table.to_excel(writer, sheet_name=f'Sheet{i+1}')


# if no arguments are provided then process all pdf files in the folder
if len(sys.argv) == 1:
    for file in os.listdir():
        if file.endswith(".pdf"):
            pdf_to_excel(file, file.replace(".pdf", ".xlsx"))
# else if check if input and output files are given
elif len(sys.argv) == 3:
    pdf_to_excel(sys.argv[1], sys.argv[2])
