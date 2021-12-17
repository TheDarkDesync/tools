import tkinter as tk
from spongetext import spongeTheText, saveTextToClipboard
from pdfmerger import *

def spongeTextAction(label, entry):
    formattedText = spongeTheText(entry.get())
    label.configure(text=formattedText)
    
def saveToClipboardAction(entry):
    formattedText = spongeTheText(entry.get())
    saveTextToClipboard(formattedText)
    
def mergePdfAction(label, entry, root):
    filenames = selectFiles()
    label.configure(text=filenames)
    tk.Button(root, text="Merge", command=lambda: saveMergedPdf(mergePdfs(filenames),entry.get())).grid(row=3, column=0, sticky="EW", pady=4)

class Tool(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class SpongeText(Tool):   
    def __init__(self, *args, **kwargs):
       Tool.__init__(self, *args, **kwargs)
       inputEntry = tk.Entry(self, width=50)
       inputEntry.grid(row= 0)
       l1 = tk.Label(self)
       l1.grid(row=1)
       tk.Button(self, text="Format", command=lambda: spongeTextAction(l1, inputEntry)).grid(row=3, column=0, sticky="EW", pady=4)
       tk.Button(self, text="Save", command=lambda: saveToClipboardAction(inputEntry)).grid(row=4, column=0, sticky="EW", pady=4)

class PdfMerger(Tool):
   def __init__(self, *args, **kwargs):
       Tool.__init__(self, *args, **kwargs)
       l1 = tk.Label(self)
       l1.grid(row=1)
       inputEntry = tk.Entry(self, width=50)
       inputEntry.grid(row= 2)
       tk.Button(self, text="Select PDFs", command=lambda: mergePdfAction(l1, inputEntry, self)).grid(row=0, column=0, sticky="EW", pady=4)
       

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        spongeText = SpongeText(self)
        pdfMerger = PdfMerger(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        spongeText.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pdfMerger.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="SpongeText", command=spongeText.show)
        b2 = tk.Button(buttonframe, text="PDF-Merger", command=pdfMerger.show)
        b3 = tk.Button(buttonframe, text="Quit", command=lambda: root.destroy())

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        spongeText.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tools")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("350x400")
    root.mainloop()