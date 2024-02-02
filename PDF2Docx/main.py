from pdf2docx import Converter
import os

pdf_name=input("Enter the name of the pdf file: ")
if not pdf_name.endswith(".pdf"):
    pdf_name=pdf_name+".pdf"
if not os.path.exists(pdf_name):
    print("File does not exist")
    exit()
    
docx_name=input("Enter the name of the docx file: ")
if not docx_name.endswith(".docx"):
    docx_name=docx_name+".docx"

try:
    cv = Converter(pdf_name)
    cv.convert(docx_name)   
    cv.close()
    print("Converted Successfully")
except:
    print("Failed To Convert")
