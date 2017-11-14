temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
s = input("请输入一串字符串，以Enter结束:")
for i in s:
    if 48 <= ord(i) <= 57:
        temp1 += 1
    elif i == ' ':
        temp2 += 1
    elif (97 <= ord(i) <= 122) or (65 <= ord(i) <= 90):
        temp3 += 1
    else:
        temp4 += 1
print("英文字母:{0}个".format(temp3))
print("数字:{0}个".format(temp1))
print("空格:{0}个".format(temp2))
print("其他字符:{0}个".format(temp4))
