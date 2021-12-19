from pikepdf import Pdf
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames

# Select .pdf files from pc
def selectFiles():
    # Create selection window
    Tk().withdraw()
    
    # Select PDFs from files
    pdfFilenames = askopenfilenames(filetypes=[("PDFs", "*.pdf")])

    # Exit if only one PDF is selected
    # if len(pdfFilenames) < 2:
    #     raise Exception("Only one file selected")
    
    return pdfFilenames

# Merge PDFs into a single PDF
def mergePdfs(pdfFilenames):
    mergedPdf = Pdf.new()
    mergedName = ""
    for pdfFile in pdfFilenames:
        src = Pdf.open(pdfFile)
        mergedName = mergedName + pdfFile.split("/")[-1].split(".")[0]
        mergedPdf.pages.extend(src.pages)
        
    return mergedPdf


# Save PDF to selected directory
def saveMergedPdf(mergedPdf, mergedName):
    saveLoc = askdirectory()
    mergedPdf.save("{dir}/{name}.pdf".format(dir=saveLoc, name = mergedName))

import sys
print(sys.path)