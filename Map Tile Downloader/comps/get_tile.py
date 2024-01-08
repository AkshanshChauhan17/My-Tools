from PIL import Image
import requests
from io import BytesIO

def display_image_from_url(image_url, img_name):
    try:
        print('image saved ->', img_name)
        response = requests.get(image_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img.save('comps/imgs/' + img_name)
    except Exception as e:
        print(f"Error: {e}")
