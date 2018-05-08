#code:utf-8
import requests
from bs4 import BeautifulSoup
import json
url = ''
filename = "urls.txt"  #用于保存解析出的url
def download(userid,count):
    url = 'https://www.douyin.com/aweme/v1/aweme/favorite/?user_id='+str(userid)+'&count='+str(count)+'&max_cursor=0&aid=1128'   #请求url
    resp = requests.get(url)  #get请求
    soup = BeautifulSoup(resp.text, 'html.parser')  #解析html
    myjson = json.loads(str(soup))     #转化为json格式数据
    with open(filename,"a+") as f:
        for i in range(count):
            video_url = myjson['aweme_list'][i]['video']['play_addr']['url_list'][0]   #提取url
            print (myjson['aweme_list'][i]['video']['play_addr']['url_list'][0])
            f.write(video_url+"\n")     #写入文件
    f.close()  #关闭文件

if __name__ == '__main__':
    download(94069666459,5)   #参数1：用户id，参数2：要下载的数量
