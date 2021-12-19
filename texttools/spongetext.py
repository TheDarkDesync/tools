import win32clipboard

# Gets the text from the clipboard 
def textFromClipboard():
    win32clipboard.OpenClipboard()
    try:
        text = list(win32clipboard.GetClipboardData())
    except TypeError:
        text = " "
    win32clipboard.CloseClipboard()
    return text

# Sponges the text
def spongeTheText(text):
    idx = 1
    for i in range(len(text)):
        if text[i].isalpha():
            if idx % 2:
                text[i] = text[i].upper()
            else:
                text[i] = text[i].lower()
            idx += 1
    
    return "".join(text)

# Puts the text to the clipboard
def textToClipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()
    
if __name__ == "__main__":
    text = textFromClipboard()
    spongedText = spongeTheText(text)
    textToClipboard(spongedText)