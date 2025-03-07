import pandas as pd
import os
import re

# Load the Excel file
file_path = "data.xlsx"  # Change this to your actual file path
df = pd.read_excel(file_path)

# Get unique addresses
address_set = set()
for index, row in df.iterrows():
    permanent_address = row["Address"]
    if pd.notna(permanent_address):  # Skip NaN values
        address_set.add(permanent_address)

address_list = list(address_set)
print(f"Unique addresses found: {len(address_list)}")

# Create directories if they don't exist
os.makedirs("filtered_data", exist_ok=True)
os.makedirs("filtered_data_pdf", exist_ok=True)

# Process each address
for address in address_list:
    # Filter data for this specific address
    address_df = df[df["Address"] == address]
    
    # Create safe filename
    safe_filename = re.sub(r'[\\/*?:"<>|]', "_", str(address))
    
    # Save as Excel
    excel_path = f"filtered_data/{safe_filename}.xlsx"
    address_df.to_excel(excel_path, index=True)
    
    # Save as PDF (requires additional libraries)
    pdf_path = f"filtered_data_pdf/{safe_filename}.pdf"
    
    # For PDF conversion, you need to install additional libraries
    try:
        # Method using pandas and openpyxl for Excel to PDF
        from openpyxl import load_workbook
        from openpyxl.utils import get_column_letter
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
        
        # Basic PDF export using reportlab (customize as needed)
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        elements = []
        
        data = [address_df.columns.tolist()] + address_df.values.tolist()
        t = Table(data)
        elements.append(t)
        
        doc.build(elements)
        print(f"Saved: {excel_path} and {pdf_path}")
    except ImportError as e:
        print(f"Saved Excel: {excel_path} (PDF conversion requires additional libraries)")
        print(f"Error saving {pdf_path}: {e}")
    except Exception as e:
        print(f"Error saving {pdf_path}: {e}")