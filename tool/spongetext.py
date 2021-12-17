import win32clipboard

# Gets the text from the clipboard 
def getTextFromClipboard():
    win32clipboard.OpenClipboard()
    try:
        text = list(win32clipboard.GetClipboardData())
    except TypeError:
        text = " "
    win32clipboard.CloseClipboard()
    return text

# Sponges the text
def spongeTheText(text):
    text = list(text)
    idx = 1
    for i in range(len(text)):
        if text[i].isalpha():
            if idx % 2:
                text[i] = text[i].upper()
            else:
                text[i] = text[i].lower()
            idx += 1

    return "".join(text)

# Saves the sponged text to the clipboard
def saveTextToClipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText("".join(text))
    win32clipboard.CloseClipboard()
