
# import module
import sys
import re
import glob
import os


'''
from pdf2image import convert_from_path
 
import sys
 
print(sys.argv[1])
# Store Pdf with convert_from_path function
images = convert_from_path(sys.argv[1])
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

'''
'''
from ironpdf import *
pdf = PdfDocument.FromFile(sys.argv[1]) 


# Extract all pages to a folder as image files
pdf.RasterizeToImageFiles("./images/*.png",DPI=96)
'''

'''
from pdf2jpg import pdf2jpg
inputpath = sys.argv[1] 
outputpath = r"./images"
print("Converting")
result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")
'''

import fitz  # PyMuPDF

def pdf_to_images(pdf_path, image_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)

        # Render the page to an image
        pix = page.get_pixmap()

        # Define the output image path
        image_path = f"{image_folder}/page_{page_number + 1}.png"

        # Save the image
        pix.save(image_path)

    # Close the PDF
    pdf_document.close()

files = glob.glob(sys.argv[1]+"/*.pdf")
print("files:", files)
for fil in files:
  print(f"Converting fil {fil} to images")
  folder=re.sub(" ","_",fil)
  folder = "images/"+".".join(folder.split(".")[:-1]) 

  if not os.path.isdir(folder):
    os.makedirs(folder)

  pdf_to_images(fil, folder) 

