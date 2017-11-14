t1 = 0
t2 = 0
t3 = 0
t4 = 0
s = input("请输入一串字符串，以Enter结束:")
for i in s:
    if 48 <= ord(i) <= 57:
        t1 += 1
    elif i == ' ':
        t2 += 1
    elif (97 <= ord(i) <= 122) or (65 <= ord(i) <= 90):
        t3 += 1
    else:
        t4 += 1
print("英文字母:{0}个".format(t3))
print("数字:{0}个".format(t1))
print("空格:{0}个".format(t2))
print("其他字符:{0}个".format(t4))
