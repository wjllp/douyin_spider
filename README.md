# douyin_spider
批量下载收藏的抖音短视频

# 使用环境
Python 3.*

# 使用方法
- 下载本项目到电脑
- 运行```pip3 install -r requirements.txt```安装所需环境
- 修改douyin.py中```main```方法中```start(args1, args2)```中的两个参数，参数1表示你的id(注意这个id并不是app中的抖音号，获取用户id的方法是进入到任意一个人的主页，然后以链接的形式分享到其他软件中，在其链接中可看到用户id)，参数2表示想要下载的数量。
- 本地执行更改```download.sh```的权限，使其具有运行权限。本地执行```sudo chmod +x download.sh```
- 文件会保存在当前目录下的video的目录中。
