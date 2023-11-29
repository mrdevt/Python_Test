import urllib3
import requests
# 执行API调用并存储响应
api='https://dev.iw233.cn/api.php?sort=iw233'
a=requests.get(api)
print(a)
# r = requests.get(url)
# 将API响应存储在一个变量中
# response_dict = a.json()
# 处理结果
# print(response_dict.keys())