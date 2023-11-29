# print('hello world')
# print(2+3)
# a=5
# b=8.9
# print(a*b)
# -i https://pypi.tuna.tsinghua.edu.cn/simple
import os
import time
import requests
from bs4 import BeautifulSoup
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
url = 'https://movie.douban.com/celebrity/1016930/photos/?type=C&start='
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
li = soup.find_all('div', attrs={'class':'cover'})
print(li)
pic_list = []
for link in li:
        pic_url = link.find('img').get('src')
        pic_url = pic_url.replace('/m/', '/l/')
        pic_list.append(pic_url)
        for i in pic_list:
                print(i)
print(len(pic_list))