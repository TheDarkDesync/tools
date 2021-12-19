from tkinter import Button, Tk
from tkinter.constants import FALSE
from pdftools import extractimgfrompdf, imgtopdf, pdfmerger, pdfsplitter
from texttools import spongetext
from webbrowser import open, get

def imageExtractorFunc():
    try:
        pdfFilename = extractimgfrompdf.selectPdf()
        extractimgfrompdf.extractImages(pdfFilename)
    except:
        print("Error: imageExtractorFunc")

def imgToPdfFunc():
    try:
        imgFilenames = imgtopdf.selectImages()
        saveLoc = imgtopdf.askdirectory(title="Select the save location of the PDF(s)")
        for imgFilename in imgFilenames:
            imgtopdf.imgToPdf(imgFilename, saveLoc)
    except:
        print("Error: imgToPdfFunc")

def pdfMergerFunc():
    try:
        pdfs = pdfmerger.selectPdfs()
        mergedPdf = pdfmerger.mergePdfs(pdfs)
        pdfmerger.savePdf(mergedPdf)
    except:
        print("Error: pdfMergerFunc")

def pdfSplitterFunc():
    try:
        pdf = pdfsplitter.selectPdf()
        pdfsplitter.splitPdf(pdf)
    except:
        print("Error: pdfSplitterFunc")

def spongeTextFunc():
    try:
        text = spongetext.textFromClipboard()
        spongedText = spongetext.spongeTheText(text)
        spongetext.textToClipboard(spongedText)
    except:
        print("Error: spongeTextFunc")
    
if __name__ == "__main__":
    root = Tk()
    root.title("Toolbox")
    root.resizable(False, False)
    root.configure(background="#0d1117")
    Button(text="TOOLBOX", font="SauceCodePro 20", background="#2ea043", activebackground="#2ea043", border=0, relief="sunken", command=lambda: open("https://bit.ly/32hnScq")).pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Image-Extractor from PDF", command=lambda: imageExtractorFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Image-To-PDF", command=lambda: imgToPdfFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="PDF-Merger", command=lambda: pdfMergerFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="PDF-Splitter", command=lambda: pdfSplitterFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Sponge-Text", command=lambda: spongeTextFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Quit Toolbox", command=lambda: root.quit(), background="#da3633", activebackground="#8d2321", border=0).pack(side="top", fill="x", padx="10", pady="10")
    root.wm_geometry("350x325")
    root.mainloop()