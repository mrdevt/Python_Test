url =' http://cq.news.cn/2021-12/13/c_1128158554.htm'
import requests
header = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
req = requests.get(url,headers=header)
req.enconding = "utf-8" #解码过程
html = req.text #导出文本内容
print(html)
print(req)
print(type(req)) 