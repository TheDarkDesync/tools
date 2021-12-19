import sys
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames
from PIL import Image

# Select imgs from files & check 
def selectFiles():
    Tk().withdraw()
    imgFilenames = askopenfilenames(title='select', filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg")])

    # Exit if only one PDF is selected
    if len(imgFilenames) < 1:
        sys.exit("You have not selected a image... Can not create PDF(s")
        
    return imgFilenames

# Converts the image into a PDF with the same name
def imgToPdf(imgFilename, saveLoc):
    name = imgFilename.split("/")[-1].split(".")[0]
    img = Image.open(imgFilename)
    imgConv = img.convert("RGB")
    imgConv.save(r"{dir}/{imgname}.pdf".format(dir=saveLoc, imgname=name))
    
if __name__ == "__main__":
    imgFilenames = selectFiles()
    saveLoc = askdirectory()
    for imgFilename in imgFilenames:
        imgToPdf(imgFilename, saveLoc)