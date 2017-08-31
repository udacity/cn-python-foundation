“””
下面的文件将会从csv文件中读取读取短信与电话，
你将在以后的课程中了解更多有关读取文件的知识。
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
"There are <count> different telephone numbers in the records.""""
