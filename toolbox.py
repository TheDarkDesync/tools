from tkinter import Button, Label, Tk
from tkinter.constants import FALSE
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askinteger
from tkinter.messagebox import askyesno
from pdftools import extractimgfrompdf, imgtopdf, pdfmerger, pdfsplitter
from texttools import spongetext
from systemtools import directorymerge
from webbrowser import open, get

def imageExtractorFunc():
    try:
        pdfFilename = extractimgfrompdf.selectPdf()
        extractimgfrompdf.extractImages(pdfFilename)
    except RuntimeError:
        print("Failed to select PDF")

def imgToPdfFunc():
    try:
        imgFilenames = imgtopdf.selectImages()
        saveLoc = imgtopdf.askdirectory(title="Select the save location of the PDF(s)")
        for imgFilename in imgFilenames:
            imgtopdf.imgToPdf(imgFilename, saveLoc)
    except RuntimeError:
        print("Failed to select image(s)")
    except PermissionError:
        print("Failed to save PDF(s)")

def pdfMergerFunc():
    try:
        pdfs = pdfmerger.selectPdfs()
        mergedPdf = pdfmerger.mergePdfs(pdfs)
        pdfmerger.savePdf(mergedPdf)
    except ValueError:
        print("Failed to save merged PDF")
    except RuntimeError:
        print("Failed to select image(s)")

def pdfSplitterFunc():
    try:
        pdf = pdfsplitter.selectPdf()
        pdfsplitter.splitPdf(pdf)
    except RuntimeError:
        print("Failed to select PDF")
    except PermissionError:
        print("Failed to save PDF(s)")

def directoryMergeFunc():
    src = askdirectory(title='Select directoy which contents you want to merge')
    dst = askdirectory(title='Select directoy where you want to merge')
    copy = askyesno('Copy instead of move?', 'Copy instead of move?')
    rec = askinteger('Recursion Depth?', 'Recursion Depth?')
    directorymerge.merge_dir(src, dst, copy, rec)


def spongeTextFunc():
    text = spongetext.textFromClipboard()
    spongedText = spongetext.spongeTheText(text)
    spongetext.textToClipboard(spongedText)

def helpFunc():
    help = Tk()
    help.title("Help")
    help.resizable(False, False)
    help.configure(background="#0d1117")
    Label(help, text="""
        SpongeText
        Formats the text from your clipboard in alternating upper and lowercase.

        PDF-Merger
        Merges the selected PDFs and saves the merged PDF to your desired location.

        PDF-Splitter
        Splits the selected PDF into the individual pages as PDFs and saves them to your desired location.

        Image to PDF
        Converts selected images to PDFs and saves them to your desired location.

        Extract Images from PDF
        Extracts all images from the selected PDF and saves them to your desired location.""", background="#0d1117", foreground="#c9d1d9", font="SauceCodePro 12", justify="left"
    ).pack(side="top", fill="x", padx="2", pady="10")
    Button(help, text="Close Help", command=lambda: help.destroy(), background="#da3633", activebackground="#8d2321", border=0, cursor="hand2").pack(side="left", padx="10", pady="10")


if __name__ == "__main__":
    root = Tk()
    root.title("Toolbox")
    root.resizable(False, False)
    root.configure(background="#0d1117")
    Button(text="TOOLBOX", font="SauceCodePro 20", background="#2ea043", activebackground="#2ea043", border=0, relief="sunken", command=lambda: open("https://bit.ly/32hnScq")).pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Image-Extractor from PDF", command=lambda: imageExtractorFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Image-To-PDF", command=lambda: imgToPdfFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="PDF-Merger", command=lambda: pdfMergerFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="PDF-Splitter", command=lambda: pdfSplitterFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Directory Merger", command=lambda: directoryMergeFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Sponge-Text", command=lambda: spongeTextFunc(), border=0, activebackground="#13233a", activeforeground="#d1e6ff", background="#afb5bb", cursor="hand2").pack(side="top", fill="x", padx="10", pady="10")
    Button(text="Help", command=lambda: helpFunc(), border=0, activebackground="#7f8387", activeforeground="#eef3ff", background="#eef3ff", cursor="hand2").pack(side="right", padx="10", pady="10")
    Button(text="Quit Toolbox", command=lambda: root.quit(), background="#da3633", activebackground="#8d2321", border=0, cursor="hand2").pack(side="left", padx="10", pady="10")
    root.wm_geometry("375x375")
    root.mainloop()
