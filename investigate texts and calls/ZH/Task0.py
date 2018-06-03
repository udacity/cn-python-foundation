"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    incoming number, answering number, time = zip(*texts)
    incoming number = incoming number[0]
    answering number = answering number[0]
    time = time[0]
print("First record of texts, {} texts {} at time {}".format(incoming number, answering number, time))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    incoming number, answering number, time, during = zip(*calls)
    incoming number = incoming number[-1]
    answering number = answering number[-1]
    time = time[-1]
    during = during[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming number, answering number, time, during number))
    
      

任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

