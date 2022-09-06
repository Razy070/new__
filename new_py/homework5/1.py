import time

import requests
from bs4 import BeautifulSoup

response = requests.get('https://picsum.photos/',
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                          "like Gecko) "
                                          "Chrome/80.0.3987.122 Safari/537.36 "
                        })

# time.sleep(1)
if response.status_code == 200:
    print('Успешно!')
    soup = BeautifulSoup(response.content, "html.parser")
    tags = soup.find_all("img")
    key = soup.select_one("img-responsive")
    url = f"https://picsum.photos/{tags[1]['src']}"

    img_data = requests.get(url).content
    with open('jpg/image_name.jpg', 'wb') as handler:
        handler.write(img_data)
