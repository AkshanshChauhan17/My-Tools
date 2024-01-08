import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

if len(sys.argv) != 3:
    print("Null")
    sys.exit(1)

input_url = sys.argv[1]
output_path = sys.argv[2]

def download_images(url, output_folder):
    response = requests.get(url)
    exp_i = 0
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                img_name = os.path.basename(urlparse(img_url).path)                    
                img_path = os.path.join(output_folder, img_name)
                try:
                    with open(img_path, 'wb') as img_file:
                        img_file.write(requests.get(img_url).content)
                except:
                    exp_i = exp_i + 1
                    print(f"EXCEPTION CASE ------------------------------- SKIP {exp_i}")
                print(f"Download: {img_name}")
        else:
            print(f"Failed to Retrieve")

download_images(input_url, output_path)