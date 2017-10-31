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
将下载好的**chromedriver_win32.zip**解压后是一个exe文件，将其复制到Chrome安装目录（通常为**C:\Program Files (x86)\Google\Chrome\Application**）

## 4 配置环境变量
1. 打开控制面板下的高级系统设置，点击**环境变量**

 ![](https://i.imgur.com/axYVodW.png)

2. 双击path,手动添加**C:\Program Files (x86)\Google\Chrome\Application\chromedriver\chromedriver.exe**，注意记得用**;**隔开

 ![](https://i.imgur.com/IkUr09N.png)

3. 确定后 **大功告成~**