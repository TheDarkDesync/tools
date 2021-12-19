from pikepdf import Pdf
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
import sys

# Select the PDF from files & check 
def selectPdf():
    Tk().withdraw()
    pdfFilename = askopenfilename(filetype=[("PDF", "*.pdf")])

    # Exit if none is selected
    if len(pdfFilename) < 1:
        sys.exit("You have not selected a PDF... Can not split")
        
    return pdfFilename

# Split the PDF into the individual pages as PDFs
def splitPdf(pdfFilename):
    saveLoc = askdirectory()
    name = pdfFilename.split("/")[-1].split(".")[0]
    pdfFile = Pdf.open(pdfFilename)
    for n, page in enumerate(pdfFile.pages):
        pdfPage = Pdf.new()
        pdfPage.pages.append(page)
        pdfPage.save("{dir}/{name}_{num}.pdf".format(dir=saveLoc, name=name, num=n))

if __name__ == "__main__":
    pdf = selectPdf()
    splitPdf(pdf)