import os
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text
    return html

def parse_html(html_text):
    soup=BeautifulSoup(html_text,'html.parser')
    pic=soup.find_all('img',)
    pic_url=pic[1].get('src')
    pic_list = []
    pic_list.append(pic_url)
    return pic_list

def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)

def main():
    pic_list = []
    for i in range(51):
        url = 'https://www.95mm.vip/83064/' + str(i) + '.html'
        html_text = get_html(url)
        pic_list += parse_html(html_text)       
    os.makedirs('D:\Python\Test\95mm\83064\\', exist_ok=True)  # 输出目录
    for i, pic_url in enumerate(pic_list):
        file_name = pic_url.split('/')[-1].split('.')[0] + '.jpg'
        file_path = 'D:\Python\Test\95mm\83064\\' + file_name
        download(file_path, pic_url)
        print('\033[7;34mdownloaded\033[0m')
    print('\033[32mComplete!\033[0m')
if __name__ == '__main__':
    main()
