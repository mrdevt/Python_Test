import os
import requests
from bs4 import BeautifulSoup
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
url='https://lab.magiconch.com/kumikos/'
html = requests.get(url, headers=headers).text
print(html)
print('------------------------------------------')
# soup = BeautifulSoup(html, 'html.parser')
# pic = soup.find_all('div', attrs={'class':'kumiko'})
# pic_list = []
# for link in pic:
#     pic_url = link.find('img').get('src')
#     pic_url = pic_url.replace('/m/', '/l/')
#     print(pic_url)
#     pic_list.append(pic_url)
# print(len(pic_list))
pic=soup.find_all()