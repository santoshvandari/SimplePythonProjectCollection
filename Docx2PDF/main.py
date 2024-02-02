from spire.doc import *
from spire.doc.common import *
import os
document = Document()
inputfilepath=input("Enter a file path: ")
if not inputfilepath.endswith(".docx"):
    inputfilepath=inputfilepath+".docx"
if not os.path.exists(inputfilepath):
    print("File does not exist")
    exit()
outputfilename=input("Enter a Output File Name: ")
if not outputfilename.endswith(".pdf"):
    outputfilename=outputfilename+".pdf"
try:
    print("Converting....")
    document.LoadFromFile(inputfilepath)
    document.SaveToFile(outputfilename, FileFormat.PDF)
    document.Close()
    print("Successfully Converted")
except:
    print("Failed to Convert!!!")