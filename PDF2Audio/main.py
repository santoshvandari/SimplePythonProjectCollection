from PyPDF2 import PdfReader
from gtts import gTTS
import os

# converting the Pdf data to text version 
def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# converting the text data to audio version
def text_to_audio(text, output_path='output.mp3', lang='en'):
    print("Converting text to audio...")
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)

# main function
if __name__ == "__main__":
    # Getting the path to the pdf file and the output audio file
    pdf_path = input("Enter the path to the PDF file: ")
    if not pdf_path.endswith('.pdf'):
        pdf_path += '.pdf'
    if not os.path.exists(pdf_path):
        print("The file does not exist.")
        exit()
    output_audio_path = input("Enter the path to the output audio file: ")
    if not output_audio_path.endswith('.mp3'):
        output_audio_path += '.mp3'
    pdf_text = pdf_to_text(pdf_path)

    # if the pdf_text is not empty then convert it to audio
    if pdf_text:
        text_to_audio(pdf_text, output_audio_path)
        print(f"Conversion successful! Audio saved as {output_audio_path}")
    else:
        print("Failed to extract text from the PDF.")
