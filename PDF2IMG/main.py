# import module
from pdf2image import convert_from_path
import os

# Store Pdf with convert_from_path function
filename=input("Enter a pdf file name: ")
if not filename.endswith('.pdf'):
    filename=filename+'.pdf'

if not os.path.exists(filename):
    print("File not found")
    exit()

if not os.path.exists('result'):
    try:
        os.makedirs('result')
    except:
        print("Cannot create directory")
        exit()

images = convert_from_path(filename)
print("Converting...")
try: 
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('result/page'+ str(i+1) +'.jpg', 'JPEG')
        print('Page '+str(i+1)+' Converted')
    print("Converted Successfully")
except:
    print("Failed to Convert")
    exit()

