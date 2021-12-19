from pikepdf import Pdf
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames
import sys

# Select PDFs from files & check 
def selectFiles():
    Tk().withdraw()
    pdfFilenames = askopenfilenames(filetypes=[("PDFs", "*.pdf")])

    # Exit if only one PDF is selected
    if len(pdfFilenames) < 2:
        sys.exit("You have only selected one PDF... Can not merge")
        
    return pdfFilenames


# Merge PDFs into a single PDF
def mergePdfs(pdfFilenames):
    mergedPdf = Pdf.new()
    mergedName = ""
    for pdfFile in pdfFilenames:
        src = Pdf.open(pdfFile)
        mergedName = mergedName + pdfFile.split("/")[-1].split(".")[0]
        mergedPdf.pages.extend(src.pages)
    
    return mergedPdf, mergedName

# Save PDF to selected directory
def savePdf(pdf, name): 
    saveLoc = askdirectory()
    pdf.save("{dir}/{name}.pdf".format(dir=saveLoc, name = name))


if __name__ == "__main__":
    pdfs = selectFiles()
    mergedPdf, name = mergePdfs(pdfs)
    savePdf(mergedPdf, name)