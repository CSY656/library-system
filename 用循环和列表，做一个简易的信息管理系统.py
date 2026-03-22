# 做一个简单的信息管理系统雏形

# 1.图书馆借书管理
# 图书馆的书籍信息登记
books = []
# 图书馆的相同书籍数量
stock = []

code = input('你是(1)管理员，(2)读者？')
if code == '1':
    # 图书馆管理员登记书籍
    while True:
        print('----------欢迎使用csy图书管理员系统-------------')
        choice = input('1.登记 2.查看 3.修改 4.删除 5.退出\n')
        if choice == '5':
            break
        elif choice == '1':
            books.append(input("登记的书籍名字："))
            stock.append(int(input('书籍的数量：')))
            continue
        elif choice == '2':
            for i in range(len(books)):
                print(f'{books[i]}书籍的库存数量为：{stock[i]}')
            continue
        elif choice == '3':
            update_name = input('输入你想修改的书籍名')
            if update_name not in books:
                print('该书籍不存在!')
                continue
            index = books.index(update_name)
            print(f'当前信息，《{books[index]}》的库存量为：{stock[index]}')
            prompt = input('修改（1）书籍名、（2）书籍数量\n')
            if prompt == '1':
                rename = input('重新修改后的书籍名：')
                books[index] = rename
            elif prompt == '2':
                number = int(input('修改书籍的数量：'))
                stock[index] = number
            continue
        elif choice == '4':
            del_name = input('输入你想要删除的书籍名')
            if del_name not in books:
                print('该书籍不存在！')
                continue
            index = books.index(del_name)
            choices = input(f'确认是否执行删除{del_name},Y/N')
            if choices.upper() == 'Y':
                books.pop(index)
                stock.pop(index)
                print('删除成功！')
            else:
                print('已取消删除操作')
            continue
elif code == '2':
    # 读者操作
    while True:
        print('----------欢迎使用csy图书读者系统---------------')
        choice = input('您想要进行什么操作？1.查阅/2.借阅/3.归还/4.退出\n')
        if choice == '4':
            break
        elif choice == '1':
            names = input('输入需要查阅的书籍名字')
            if names not in books:
                print('该书籍不存在！')
                continue
            index = books.index(names)
            print(f'你要查阅的书籍{books[index]}')
            continue
        elif choice == '2':
            names = input('输入需要借阅的书籍名字')
            if names not in books:
                print('该书籍不存在！')
                continue
            index = books.index(names)
            prompt = input(f'《{books[index]}》还剩{stock[index]}本,是否借阅？Y/N')
            if prompt.upper() == 'Y':
                if stock[index] > 0:
                    stock[index] -= 1
                    print(f'{names}借出成功')
                else:
                    print("该书籍库存量不足")
            continue
        elif choice == '3':
            names = input('输入需要归还的书籍名字')
            if names not in books:
                print(f'《{names}》不是本馆书籍')
                continue
            prompt = input(f'是否确认归还？Y/N')
            if prompt.upper() == 'Y':
                index = books.index(names)
                stock[index] += 1
                print(f'归还成功,《{books[index]}》剩余{stock[index]}本')
            continue
else:
    print('输入错误，请重新输入：1.管理员，2.读者')






