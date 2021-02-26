import requests
from bs4 import BeautifulSoup
import os 
file_name = input('请输入文件夹的名字:') # 定义文件夹名字
os.makedirs(file_name) # 建立文件夹
image_url = [] # 创建一个储存图片url的列表
url = 'https://image.baidu.com/search/index?' # 爬取图片的地址
# 定义请求头
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

pic_featuer = input("输入图片类型:") # 设置一个图片名字变量
os.system('clear') # 清屏
pic_num = int(input("输入图片张数*30:")) # 设置一个图片张数变量
for picture_num in range(pic_num):
    # 请求的变量参数
    pra = {
        'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'queryWord': str(pic_featuer),
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '-1',
    'z': '',
    'ic':'', 
    'hd': '',
    'latest':'', 
    'copyright':'', 
    'word': str(pic_featuer),
    's': '',
    'se':'' ,
    'tab': '',
    'width':'', 
    'height': '',
    'face': '0',
    'istype': '2',
    'qc':'', 
    'nc': '1',
    'fr':'', 
    'expermode':'', 
    'force': '',
    'pn': (int((int(pic_num)+1)*30)),
    'rn': '30',
    'gsm': '78',
    '1599038493833':'',
    }
# 进行图片地址爬取
res = requests.get(url, headers=headers, params=pra)
# json数据将其返回一个json解析对象
res_json = res.json()
pic_urls =  res_json['data'] # 提取data索引下面的值
try:
    for url in pic_urls: # 遍历dada
        url_hover = url['hoverURL'] # 找data下面的hoverURL参数
        print(url_hover) # 对hoverURl参数进行打印
        image_url.append(url_hover)  # 将获取到的值储存在image_url列表中    
except KeyError:
    pass  

count_num = 0  # 定义一个count变量作为图片的名字
for res_url in image_url:
    try: 
        res_image  = requests.get(res_url, headers= headers) # 对图片地址进行爬取
    except requests.exceptions.MissingSchema:
        pass
    res_content = res_image.content # 将爬取到的数据进行二进制化
    count_num+=1 # 每经过一次循环count_num自加一
    image_path = file_name+'/test'+str(count_num)+'.jpg'
    image_files = open(image_path, 'wb')  # 储存图片
    image_files.write(res_content) # 写入图片
    image_files.close()

    
       