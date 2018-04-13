## 一、在windows上安装

## 1 安装selenium
1. 启动**cmd命令行**（同时按住**windows键**和**R键**，在对话框内输入*cmd*，然后回车）

2. 安装**selenium**，在弹出的窗口内输入
	>pip install selenium

## 2 下载chromedrive
前往 [**chromedriver 下载页面**](https://sites.google.com/a/chromium.org/chromedriver/downloads)

![](https://i.imgur.com/2JoXcSU.png)

（如果官网下载网页无法访问，你可以访问[**Udacity**](https://cn.udacity.com)的[**GitHub项目**](https://github.com/DaemonFG/IntrotoPython-Think-Tank/blob/master/P2/ChromeDriver_Download.md)）

选择最新的win版本**chromedriver_win32.zip**

![](https://i.imgur.com/3UBl9pD.png)

## 3 解压文件
将下载好的**chromedriver_win32.zip**解压后是一个exe文件，将其复制到Python安装目录

### 注意 安装目录找不到怎么办
1. 打开控制面板下的高级系统设置，点击**环境变量**

 ![](https://i.imgur.com/axYVodW.png)

2. 双击path,里面带python那个就是了（例如**C:\Users\Big Geng\AppData\Local\Programs\Python\Python36**）

## 二、Mac版快速配置指南

## 1 下载同Windows

前往 [**chromedriver 下载页面**](https://sites.google.com/a/chromium.org/chromedriver/downloads)

![](https://i.imgur.com/2JoXcSU.png)

（如果官网下载网页无法访问，你可以访问[**Udacity**](https://cn.udacity.com)的[**GitHub项目**](https://github.com/DaemonFG/IntrotoPython-Think-Tank/blob/master/P2/ChromeDriver_Download.md)）

## 2 找到包含lib关键字的路径

![](https://i.imgur.com/Ka1Qf0K.jpg)

## 3 放到跟lib同一级目录下的bin里

![](https://i.imgur.com/AUW2BcG.jpg)

   同理，如果使用pyenv，放在自己建立的环境下的bin目录中即可
   
   ![](https://i.imgur.com/Rm8aOL3.jpg)
