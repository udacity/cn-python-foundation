# 在windows上安装 selenium 和 chromedriver

## 1 安装selenium
1. 启动**cmd命令行**（同时按住**windows键**和**R键**，在对话框内输入*cmd*，然后回车）

2. 安装**selenium**，在弹出的窗口内输入
	>pip install selenium

## 2 下载chromedrive
前往 [chromedriver 下载页面](https://sites.google.com/a/chromium.org/chromedriver/downloads)

![](https://i.imgur.com/2JoXcSU.png)

选择最新的win版本**chromedriver_win32.zip**

![](https://i.imgur.com/3UBl9pD.png)

## 3 解压文件
将下载好的**chromedriver_win32.zip**解压后是一个exe文件，将其复制到Python安装目录

### 注意 安装目录找不到怎么办
1. 打开控制面板下的高级系统设置，点击**环境变量**

 ![](https://i.imgur.com/axYVodW.png)

2. 双击path,里面带python那个就是了（例如**C:\Users\Big Geng\AppData\Local\Programs\Python\Python36**）
