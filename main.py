import PyPDF2
import pyttsx3

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def text_to_audio(text, output_path='output.mp3'):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = input("Enter the path of the PDF file: ")
    output_audio_path = input("Enter the desired output MP3 file name (optional, default is 'output.mp3'): ") or 'output.mp3'

    pdf_text = pdf_to_text(pdf_path)

    if pdf_text:
        text_to_audio(pdf_text, output_audio_path)
        print(f"Conversion successful! Audio saved as {output_audio_path}")
    else:
        print("Failed to extract text from the PDF.")
