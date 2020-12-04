from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen, Request, urlretrieve
import urllib
import os
import traceback

# Scraping line sticker
URL = 'https://store.line.me/stickershop/product/6697817/en?from=sticker'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Get the wanted components
results = soup.findAll('div', {'class': 'mdCMN09LiInner FnImage'})
# result = soup.find_all("div", class_='mdCMN09LiInner FnImage')

image_links = []
i = 1
# Get the component with the image link
for result in results:
    temp = result.find("span")['style']
    image_links = re.findall('https\S*.png', temp)

    # create result folder
    if not os.path.exists("sticker"): os.mkdir("sticker")
    
    # Save picture from retrieved link
    try:
        urllib.request.urlretrieve(
            image_links[0], 'sticker/shiba' + str(i) + '.png')
    except Exception as e:
        print('Image Not Found')
        error_msg = ''.join(traceback.format_exception(
            etype=type(e), value=e, tb=e.__traceback__))
        print(error_msg)

    i += 1
