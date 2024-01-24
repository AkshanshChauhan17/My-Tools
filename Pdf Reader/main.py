import requests
import PyPDF2

def read_pdf_from_web(pdf_url):
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        with open('downloaded_pdf.pdf', 'wb') as file:
            file.write(response.content)
        
        return read_pdf('downloaded_pdf.pdf')
    else:
        print(f"Failed to download PDF from {pdf_url}. Status code: {response.status_code}")
        return None



def read():
    try:
        pdf_url = "https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId=120"
        pdf_text = read_pdf_from_web(pdf_url)
        
        if pdf_text:
            print(pdf_text)
    except:
        print("Unreadable")