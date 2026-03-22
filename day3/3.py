num = int(input('请输入3位正整数：'))
a = num // 100  # 百位
b = num // 10 % 10 # 十位
c = num % 10  # 个位
if num == (a ** 3) + (b ** 3) + (c ** 3):
    print('这是一个水仙花数')
else:
    print('这不是一个水仙花数')
