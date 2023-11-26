import os
import time
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text
    print('get_html')
    return html

def parse_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    pic = soup.find_all('img')
    pic_list = []
    for link in pic:
        pic_url = link.find('img').get('src')
        pic_url = pic_url.replace('/m/', '/l/')
        pic_url='http://www.weibomn.com/'+pic_url
        pic_list.append(pic_url)
    return pic_list

def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)
    print('download')

def main():
    pic_list = []
    url = 'http://www.weibomn.com/post_725.html'
    html_text = get_html(url)
    pic_list += parse_html(html_text)       
    os.makedirs('./weibomn/725/', exist_ok=True) 
    for i, pic_url in enumerate(pic_list):
        file_name = pic_url.split('/')[-1].split('.')[0] + '.jpg'
        file_path = './weibomn/725/' + file_name
        download(file_path, pic_url)
        print(file_name)
        print('\033[7;34mdownloaded\033[0m')
    print('\033[32mComplete!\033[0m')

if __name__ == '__main__':
    main()