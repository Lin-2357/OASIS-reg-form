import pyperclip
from pdfparse import checkClause

filename = pyperclip.paste()

if filename:
    if filename[-4:] != '.pdf':
        filename += '.pdf'
    checkClause(filename)
else:
    print("File Name Invalid")