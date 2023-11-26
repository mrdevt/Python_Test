import os
import requests
from bs4 import BeautifulSoup
def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text
    return html
# def parse_html(html_text):
#     soup = BeautifulSoup(html_text, 'html.parser')
#     req = soup.find_all('img', )
#     pic_list = []
#     for i in range(35):
#         pic_url = req[i].get('src')
#         pic_list.append(pic_url)
#         # print(pic_url.split('/')[-1].split('.')[0] + '.jpg')
#     return pic_list
def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
    }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)
def main():
    os.makedirs('D:\Python\Test\welfarehub\\', exist_ok=True)
    for i in range(43):
        url = 'https://welfarehub.net/2.html?page=' + str(i)
        soup = BeautifulSoup(get_html(url), 'html.parser')
        req = soup.find_all('img', )
        pic_list = []
        for r in range(35):
            pic_url = req[r].get('src')
            pic_list.append(pic_url)
      # 输出目录
        for p, pic_url in enumerate(pic_list):
            file_name = pic_url.split('/')[-1].split('.')[0] + '.jpg'
            file_path = 'D:\Python\Test\welfarehub\\' + file_name
            download(file_path, pic_url)
            print('\033[7;34m'+file_name+'\033[0m')
    print('\033[32mComplete!\033[0m')
if __name__ == '__main__':
    main()