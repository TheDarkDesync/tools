from pikepdf import Pdf
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames
import sys

# Select PDFs from files & check 
Tk().withdraw()
pdfs = askopenfilenames(filetypes=[("PDFs", "*.pdf")])

# Exit if only one PDF is selected
if len(pdfs) < 2:
    sys.exit("You selected only one PDF... Can not merge")

# Merge PDFs into a single PDF
mergedPdf = Pdf.new()
mergedName = ""
for pdf in pdfs:
    src = Pdf.open(pdf)
    mergedName = mergedName + pdf.split("/")[-1].split(".")[0]
    mergedPdf.pages.extend(src.pages)

# Save PDF to selected directory
saveLoc = askdirectory()
mergedPdf.save("{dir}/{name}.pdf".format(dir=saveLoc, name = mergedName))
