from rembg import remove
from PIL import Image
import os

# input_path = 'input.jpeg'
input_path = (input("Enter a Image Name(with Extension): ")).lower().strip()
if not (input_path and input_path.endswith((".jpeg",".jpg",".png"))):
    print("Invalid File Name.")
    exit(1)
if not os.path.exists(input_path):
    print("File Doesn't Exists.")
    exit(1)
# output_path = 'output.png'
output_path=input("Enter a Output File Name: ")
if not output_path.endswith(".png"):
    if not output_path:
        output_path = input_path.split(".")[0]
    output_path+=".png"

try:
    print("Removing Background...")
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    print("Background Removed Successfully.")
except Exception as e:
    print("Failed to Remove Background. Error: ", e)
    exit(1)