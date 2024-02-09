import os 
from PIL import Image 

file_name=input("Enter a File Name(.jpg): ")
if not file_name.endswith('.jpg'):
	file_name+='.jpg'
if not os.path.exists(file_name):
	print("File not found")
	exit(1)
output_name=input("Enter a output file name: ")
if not output_name.endswith('.jpg'):
	output_name+='.jpg'
compresslevel=input("Enter a Percentage to Compress(0-100): ")
if compresslevel.endswith("%"):
	compresslevel=compresslevel.split("%")[0]
compresslevel=int(compresslevel)


try:
	print("Compressing the Images....")
	picture = Image.open(file_name) 
	picture.save(output_name,"JPEG",optimize = True,quality = (100-compresslevel))
	print("Compression Successful....")
except Exception as ex:
	print(f"Error While Compressing. Error: {ex}")	
	exit(1)
