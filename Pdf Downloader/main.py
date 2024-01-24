import requests
import threading
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

def download_pdf(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully and saved at {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

def runner1(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner2(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner3(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner4(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner5(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner6(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")


def runner7(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner8(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner9(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

def runner10(s, e):
    for i in range(int(s), int(e)):
        try:
            pdf_url = f"https://online.uktech.ac.in/ums/Print/DownloadPDFPromotionApplicatinForm?StudentPromotionId={i}"
            save_path = str(i) + '.pdf'
            download_pdf(pdf_url, save_path)
            print(i, "Downloaded Successfully")
        except:
            print(i, "Downloaded Unsuccessfully")

t1 = threading.Thread(target=runner1(start, end/10))
t2 = threading.Thread(target=runner2(end/10, end/9))
t3 = threading.Thread(target=runner3(end/9, end/8))
t4 = threading.Thread(target=runner4(end/8, end/7))
t5 = threading.Thread(target=runner5(end/7, end/6))
t6 = threading.Thread(target=runner6(end/6, end/5))
t7 = threading.Thread(target=runner7(end/5, end/4))
t8 = threading.Thread(target=runner8(end/4, end/3))
t9 = threading.Thread(target=runner9(end/3, end/2))
t10 = threading.Thread(target=runner10(end/2, end))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

print("TASK COMPLETED")