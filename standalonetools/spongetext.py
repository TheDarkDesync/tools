import win32clipboard

win32clipboard.OpenClipboard()
try:
    text = list(win32clipboard.GetClipboardData())
except TypeError:
    text = " "
win32clipboard.CloseClipboard()

idx = 1
for i in range(len(text)):
    if text[i].isalpha():
        if idx % 2:
            text[i] = text[i].upper()
        else:
            text[i] = text[i].lower()
        idx += 1

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("".join(text))
win32clipboard.CloseClipboard()
