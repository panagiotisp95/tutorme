from PIL import Image
import requests
from io import BytesIO


class PictureDownloader:
    def get_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    def store_image(self, img, name):
        img.save(name)
