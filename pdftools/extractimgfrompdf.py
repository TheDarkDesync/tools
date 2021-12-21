import os
import sys
from pikepdf import Pdf, PdfImage
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename

# Select the PDF from files & check 
def selectPdf():
    Tk().withdraw()
    pdfFilename = askopenfilename(title="Select the PDF where you want to extract images", filetype=[("PDF", "*.pdf")])

    # Exit if none is selected
    if len(pdfFilename) < 1:
        # sys.exit("You have not selected a PDF... Can not extract images")
        raise RuntimeError
        
    return pdfFilename

# Extracts all images from the selected PDF
def extractImages(pdfFilename):
    saveLoc = askdirectory(title="Select the save location for the extracted images")
    makeDir(saveLoc)
    pdf = Pdf.open(pdfFilename)
    pageCount = 0
    for page in pdf.pages:
        imagesList = list(page.images)
        if len(imagesList) != 0:
            for image in imagesList:
                pdfImage = PdfImage(page.images[image])
                rawImage = pdfImage.as_pil_image()
                name = "{docname}_{pagenum}_{imgnum}".format(docname=pdfFilename.split("/")[-1].split(".")[0].replace(" ", "_"),pagenum=pageCount, imgnum=image.replace("/", ""))
                rawImage.save(r"{dir}/extractedImages/{imgname}.png".format(dir=saveLoc, imgname=name))
        pageCount += 1

# Creates folder/directory for the extracted images (if not already exsits)
def makeDir(path):
    path = path + "/extractedImages"
    try:
        os.mkdir(path)
    except OSError:
        print("Directory already exists")

if __name__ == "__main__":
    pdfFilename = selectPdf()
    extractImages(pdfFilename)