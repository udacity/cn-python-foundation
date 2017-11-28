"""
下面的文件将会从csv文件中读取读取短信与电话记录，
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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""

#统计打电话数据
def countingCaller(calls):
    result = {}
    for call in calls:
        caller = call[0].strip()
        receiver = call[1].strip()

        if caller in result:
            result[caller]['call'] += 1
        else:
            result[caller] = {}
            result[caller]["call"] = 1
            result[caller]["receive"] = 0

        if receiver in result:
            result[receiver]["receive"] += 1
        else:
            result[receiver] = {}
            result[receiver]["receive"] = 1
            result[receiver]["call"] = 0
    return result

#统计发短信信息
def countingTexter(texts):
    result = {}
    for text in texts:
        sender = text[0].strip()
        receiver = text[1].strip()

        if sender in result:
            result[sender]['send'] += 1
        else:
            result[sender] = {}
            result[sender]["send"] = 1
            result[sender]["receive"] = 0

        if receiver in result:
            result[receiver]["receive"] += 1
        else:
            result[receiver] = {}
            result[receiver]["receive"] = 1
            result[receiver]["send"] = 0
    return result


def findSellerPhone(callers,messagers):
    result = [] #销售电话
    for caller in callers:
        # 找出只打电话从没收到电话的号码
        if (callers[caller]['call'] > 0) and (callers[caller]['receive'] == 0):
            # 查找此号码是否收发短信
            if (caller not in messagers) :
                result.append(caller)
    result.sort()
    return result


callers = countingCaller(calls)
messagers = countingTexter(texts)

print("These numbers could be telemarketers: ")
print("\n".join(findSellerPhone(callers,messagers)))
# print(result)
# print(countingTexter(texts))