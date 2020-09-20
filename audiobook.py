import pyttsx3
import PyPDF2
import PyPDF4
from tkinter.filedialog import *
book = askopenfilename()
#pdfreader =PyPDF2.PdfFileReader(book)
pdfreader =PyPDF4.PdfFileReader(book)
pages = pdfreader.numPages
for num in range (0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player =pyttsx3.init()
    player.say(text)
    player.runAndWait()