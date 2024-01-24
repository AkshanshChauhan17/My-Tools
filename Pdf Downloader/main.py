import requests

def download_pdf(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully and saved at {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

for i in range(1, 100):
    try:
        pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
        save_path = str(i) + '.pdf'
        download_pdf(pdf_url, save_path)
        print(i, "Downloaded Successfully")
    except:
        print(i, "Downloaded Unsuccessfully")
