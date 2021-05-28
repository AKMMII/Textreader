import pyttsx3          #   pip install pyttsx3
import PyPDF2           #pip install PyPDF2
book = open('.pdf', 'rd')           # add any .pdf books
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):         # for reapte any page
    page = pdfReader.getPage(5)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndwait()



