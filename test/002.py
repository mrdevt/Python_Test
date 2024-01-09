# url =' http://cq.news.cn/2021-12/13/c_1128158554.htm'
# import requests
# header = {"User-Agent":
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
# req = requests.get(url,headers=header)
# req.enconding = "utf-8" #解码过程
# html = req.text #导出文本内容
# print(html)
# print(req)
# print(type(req)) 
import matplotlib.pyplot as plt
x = list(range(1100))
y = [1] * 1100

plt.subplots(figsize=(18,6))
time_label=[]
plt.xlabel('time')                         # 设置x坐标轴的名称
my_tick = list(range(1100))                # 可以用list(range(len(my_label))) 替代
my_label = time_label[0:1100]               # 有1100个时间字符串的list
plt.grid(b=True)                                        
plt.xticks(my_tick[::100],my_label[::100],rotation=60, ha='right')              # 利用切片来完成需求
plt.ylabel('whatever')                                   
plt.plot(x, y)    
plt.show()                                      
