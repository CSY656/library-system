user = input('请输入用户名：')
password = input('请输入密码：')

if user == 'root' and password == '123456':
    print('登陆成功')
else:
    print('登陆失败')