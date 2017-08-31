"""
Python入门 项目 1, 任务 1

完成该任务的文件中的每个任务. 以压缩文件提交整个文件夹或是GitHub repo。
在项目准备页面上有完整的提交说明。
"""


"""
读取短信与电话。
如果你不知道如何读取文件，也是可以的
你将在以后的课程中了解更多有关阅读文件的知识
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1： 
记录中一共有多少电话号码？
输出信息：
"记录中一共有<多少>个电话号码"
"""
