from PIL import Image
import requests
from io import BytesIO

def display_image_from_url(image_url, index):
    try:
        print('image saved ->', index)
        response = requests.get(image_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img.save('comps/imgs/' + str(index) + '.png')
    except Exception as e:
        print(f"Error: {e}")
