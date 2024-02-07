import img2pdf
import os
import pathlib



file_path=input("Enter the Name of the Images(Provide Space between if more than One Images): ")
ImagesCollections = list(filter(None,(file_path.split(" "))))
print(ImagesCollections)

# check that every data file is ends with .jpg and add .jpg if not ends with .jpg
for i in ImagesCollections:
	if not i.endswith(".jpg"):
		ImagesCollections[ImagesCollections.index(i)] = i + ".jpg"

# check that the file exist or not 
for i in ImagesCollections:
	if not os.path.exists(i):
		print(f"File {i} not found")
		exit(1)

output_file = input("Enter the Name of the Output File: ")
if not output_file.endswith(".pdf"):
	output_file = output_file + ".pdf"

try:
	with open(output_file,"wb") as f:
		print("Converting to PDF...")
		f.write(img2pdf.convert(ImagesCollections))
		print("PDF Created Successfully")
except Exception as e:
	print("Failed to Convert to PDF")
