#code:utf-8
import requests
from bs4 import BeautifulSoup
import json
session = requests.session()
#保存url的文件名
filename = "urls.txt"
def start(userid,count):
    #一次请求最多能获取到的url数
    maxCount = 35
    #计算出需要发送多少次请求（向上取整）
    page = int((count + maxCount - 1) / maxCount)
    #初始游标为0
    max_cursor = 0
    for i in range(0,page):
        #如果需获取的视频数大于最大能获取的数，则传入maxCount，并减小count的值
        if (count > maxCount):
            max_cursor = download(userid,maxCount,max_cursor)
            count = count - maxCount
        #最后count被减到小于maxCount的时候，传入count
        else:
            max_cursor = download(userid,count,max_cursor)        

#参数：用户id，用于下载指定用户的收藏视频。count：下载数量。max_cursor：游标
def download(userid,count,max_cursor):
    url = 'https://www.douyin.com/aweme/v1/aweme/favorite/?user_id='+str(userid)+'&count='+str(count+1)+'&max_cursor='+str(max_cursor)+'&aid=1128'
    #get请求，并保存响应报文
    resp = session.get(url)
    #解析http报文
    soup = BeautifulSoup(resp.text, 'html.parser')
    #解析json
    myjson = json.loads(str(soup))
    #获取游标，用于解析下一页视频
    max_cursor = myjson['max_cursor']
    with open(filename,"a+") as f:
        for i in range(0,count):
            #解析json数据
            video_url = myjson['aweme_list'][i]['video']['play_addr']['url_list'][0]
            print (myjson['aweme_list'][i]['video']['play_addr']['url_list'][0])
            #写入文件
            f.write(video_url+"\n")
    #关闭文件
    f.close()
    #返回游标
    return max_cursor
if __name__ == '__main__':
    #参数一：用户id，参数2：你想下载的视频个数
    start(84064249580,100)
