"""
Python入门 项目 1, 任务 0

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
任务0: 
短信的第一条记录是什么？最后一条记录是什么？
输出信息: 
"第一条短信记录, <发送方电话号码> 给 <接收方电话号码> 在 <什么时间>发送了短信"
"最后一条通话记录, <拨号方电话号码> 给 <接收方电话号码> 在 <什么时间>拨打了电话, 通话持续了 <多少> 秒"
"""

