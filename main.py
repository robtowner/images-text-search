import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    # folder where the images of invoices are stored (CHANGE TO YOUR DESIRED FOLDER)
    path = "C:\\Users\\Rob T\\PycharmProjects\\image\\invoices"

    # path to output text file - all images containing searched keyword (CHANGE TO YOUR DESIRED FOLDER)
    fullTempPath = "C:\\Users\\Rob T\\PycharmProjects\\image\\invoices\\outputFile.txt"

    # running through the images inside the folder
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)

        # applying ocr using pytesseract for python
        text = pytesseract.image_to_string(img, lang="eng")

        # Keyword search (brand, product). After every search, you will need to delete the output file to run again
        searchword = "cHurch"

        if searchword.lower() in text.lower():

        # saving the text for appending it to the output.txt file
        # a + parameter used for creating the file if not present
        # and if present then append the text content
            file1 = open(fullTempPath, "a+")

        # providing the name of the image
            file1.write(imageName + "\n")

        # providing the content in the image
            file1.write(text + "\n")
            file1.close()

        # for printing the output file
            file2 = open(fullTempPath, 'r')
            print(file2.read())
            file2.close()

if __name__ == '__main__':
  main()