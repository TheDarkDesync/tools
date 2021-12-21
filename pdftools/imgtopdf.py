import sys
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames
from PIL import Image

# Select imgs from files & check 
def selectImages():
    Tk().withdraw()
    imgFilenames = askopenfilenames(title="Select the image(s) you want to convert to PDF", filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg")])

    # Exit if only one PDF is selected
    if len(imgFilenames) < 1:
        # sys.exit("You have not selected a image... Can not create PDF(s")
        raise RuntimeError
        
    return imgFilenames

# Converts the image into a PDF with the same name
def imgToPdf(imgFilename, saveLoc):
    name = imgFilename.split("/")[-1].split(".")[0]
    img = Image.open(imgFilename)
    imgConv = img.convert("RGB")
    imgConv.save(r"{dir}/{imgname}.pdf".format(dir=saveLoc, imgname=name))
    
if __name__ == "__main__":
    imgFilenames = selectImages()
    saveLoc = askdirectory(title="Select the save location of the PDF(s)")
    for imgFilename in imgFilenames:
        imgToPdf(imgFilename, saveLoc)