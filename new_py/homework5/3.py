import json
import time
from threading import Thread

from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Safari/537.36"}


def get_img(i):
    url = f"{i['url']}"
    response = requests.get('https://picsum.photos/',
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                              "like Gecko) Chrome/80.0.3987.122 Safari/537.36 "
                            })

    if response.status_code == 200:
        print('Успешно!')
        soup = BeautifulSoup(response.content, "html.parser")
        tags = soup.find_all("img")
        key = soup.select_one("img-responsive")
        url = f"https://picsum.photos/{tags[1]['src']}"

        img_data = requests.get(url).content
        with open(f'jpg/{i["id"]}.png', 'wb') as handler:
            handler.write(img_data)


with open('txt/data.txt', 'r') as fp:
    nums = fp.read()
    obj = json.loads(nums)
    for i in obj:
        print(i['url'])
        print(i)

        if i['id'] < 5:
            th = Thread(target=get_img, args=(i,))
            th.start()
        if i['id'] > 20:
            break
