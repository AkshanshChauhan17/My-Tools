import requests
import PyPDF2

def read_pdf_from_web(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        with open('downloaded_pdf.pdf', 'wb') as file:
            file.write(response.content)
        
        return read_pdf('downloaded_pdf.pdf')
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF from {pdf_url}: {e}")
        return None

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = pdf_reader.numPages

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text

# Example usage:
pdf_url = "https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId=7"  # Replace with the actual URL of the PDF
pdf_text = read_pdf_from_web(pdf_url)

if pdf_text:
    print(pdf_text)
