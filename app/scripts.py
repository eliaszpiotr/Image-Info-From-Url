import requests
from PIL import Image
from io import BytesIO
from colorthief import ColorThief


def get_image_size(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))
    return im.size


def dominantcolor(id):
    color_thief = ColorThief(f'app/images/img{id}.jpg')
    dominant_color = color_thief.get_color(quality=1)
    dominant_color_hex = '#%02x%02x%02x' % dominant_color
    return dominant_color_hex


def save_image(url, id):
    img_data = requests.get(url).content
    with open(f'app/images/img{id}.jpg', 'wb') as handler:
        handler.write(img_data)
