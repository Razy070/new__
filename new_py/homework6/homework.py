# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="https://www.banki.ru/products/currency/cb/", headers=headers)
# print(response.text)
#
# with open('new.html', mode='wb') as file:
#     file.write(response.content)


#################################################

# import requests
#
# while True:
#     url = 'https://picsum.photos/300/300/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers, timeout=10)
#     with open('1/new.jpg', mode='wb') as file:
#         file.write(response.content)


##############################################

# import requests
#
# r = requests.get('https://goweather.herokuapp.com/weather/Curitiba')
# print(r.json())
