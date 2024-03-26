from textblob import TextBlob
import os

def main():
    filename=input("Enter a File Name For the Correction(Example: data.txt): ")
    if not filename.endswith('.txt'):
        filename = filename + '.txt'

    if not os.path.exists(filename):
        print("File Not Found")
        exit()

    resultname=input("Enter a File Name of result: ")
    if not resultname.endswith('.txt'):
        resultname = resultname + '.txt'

    try: 
        print("Reading the Data....")
        with open(filename, 'r') as file:
            text = file.read()
            if not text:
                print("File is Empty")
                exit()
        blob = TextBlob(text)
        print("Correcting the data....")
        correct = str(blob.correct())
        with open(resultname,'w') as file:
            file.write(correct)
        print("File Corrected Successfully.")
    except Exception as e:
        print(e)
        print("Error in correcting the file")

if __name__ == "__main__":
    main()