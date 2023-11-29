import os
import re
import requests

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    html = requests.get(url, headers=headers).text

    return html

def parse_html(html_text):
    picre = re.compile(r'[a-zA-z]+://[^\s]*\.jpg')  # 本正则式得到.jpg结尾的url
    pic_list = re.findall(picre, html_text)

    return pic_list

def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
        }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)

def main():
    # 使用时修改url即可
    url = 'http://xyz.com/series'
    html_text = get_html(url)
    pic_list = parse_html(html_text)

    os.makedirs('./pic/', exist_ok=True)  # 输出目录
    for pic_url in pic_list:
        file_name = pic_url.split('/')[-1]
        file_path = './pic/' + file_name

        download(file_path, pic_url)


if __name__ == '__main__':
    main()