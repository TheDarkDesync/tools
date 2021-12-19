from pikepdf import Pdf
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
import sys

# Select PDFs from files & check 
def selectPdfs():
    Tk().withdraw()
    pdfFilenames = askopenfilenames(title="Select the PDFs you want to merge", filetypes=[("PDFs", "*.pdf")])

    # Exit if only one PDF is selected
    if len(pdfFilenames) < 2:
        sys.exit("You have only selected one PDF... Can not merge")
        
    return pdfFilenames

# Merge PDFs into a single PDF
def mergePdfs(pdfFilenames):
    mergedPdf = Pdf.new()
    for pdfFile in pdfFilenames:
        src = Pdf.open(pdfFile)
        mergedPdf.pages.extend(src.pages)
    
    return mergedPdf

# Save PDF to selected directory
def savePdf(pdf): 
    saveNameLoc = asksaveasfilename(title="Select the save location and name of the merged PDF", defaultextension=".pdf")
    pdf.save(saveNameLoc)

if __name__ == "__main__":
    pdfs = selectPdfs()
    mergedPdf= mergePdfs(pdfs)
    savePdf(mergedPdf)