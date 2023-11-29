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
    soup = BeautifulSoup(html_text, 'html.parser')
    li = soup.find_all('div', attrs={'class':'cover'})
    pic_list = []
    for link in li:
        pic_url = link.find('img').get('src')
        pic_url = pic_url.replace('/m/', '/l/')
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
    '从豆瓣下载石原里美图片，观察发现每页包含30张图片，其url按30递增，如下所示'
    pic_list = []
    for i in range(10):
        url = 'https://movie.douban.com/celebrity/1016930/photos/?type=C&start=' + str(30*i) + '&sortby=like&size=a&subtype=a'
        html_text = get_html(url)
        pic_list += parse_html(html_text)
        
    os.makedirs('./pic/', exist_ok=True)  # 输出目录

    for i, pic_url in enumerate(pic_list):
        if i%30 == 0:
            print('正在下载第%s页'%(i/30+1))
        file_name = pic_url.split('/')[-1].split('.')[0] + '.jpg'
        file_path = './pic/' + file_name

        download(file_path, pic_url)


if __name__ == '__main__':
    main()