from PyPDF2 import PdfReader 
import glob

pdf_list = glob.glob("*.pdf")

for pdf in pdf_list:
    reader = PdfReader(pdf) 
    page_length = len(reader.pages) 

    if page_length == 0:
        print("__null__")
    else:
        page = reader.pages[0] 
        text = page.extract_text().split("\n")[11]
        print(text)