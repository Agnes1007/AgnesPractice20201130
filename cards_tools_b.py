cards_list = []


def show_menu():
    """显示功能菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def cards_new():
    """新建名片"""
    print("新建名片")
    print("*" * 50)

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")

    cards_dict = {"name":name_str,
                  "phone":phone_str,
                  "qq":qq_str,
                  "email":email_str}
    cards_list.append(cards_dict)
    print(cards_list)
    print("%s 名片创建成功！" % name_str)


def show_cards():
    """显示全部名片信息"""

    print("显示所有名片信息")
    print("*" * 50)

    if len(cards_list) == 0:
        print("当前没有任何名片信息，请使用新建名片功能新建名片！")
    else:
        print("姓名",end="\t\t")
        print("电话", end="\t\t")
        print("QQ", end="\t\t")
        print("邮箱", end="\t\t")
        print("")

        for cards_dict in cards_list:
            for k in cards_dict:
                print(cards_dict[k],end="\t\t")
            print("")


def search_cards():
    """查询名片信息"""

    print("查询名片")
    print("*" * 50)
    if len(cards_list) == 0:
        print("当前还没有名片")
        return

    name = input("请输入要查询名片的姓名：")
    for cards_dict in cards_list:
        if name == cards_dict["name"]:
            for name_t in ["姓名", "电话", "QQ", "邮箱"]:
                print(name_t,end="\t\t")
            print("")

            print("%s\t\t%s\t\t%s\t\t%s" % (name,
                                            cards_dict["phone"],
                                            cards_dict["qq"],
                                            cards_dict["email"]))

            while True:

                action_s = input("请输入对名片的操作：1：修改/ 2：删除/ 0：返回上级菜单")
                print("您的选择是：%s" % action_s)

                if action_s == "1":
                    modify_card()

                elif action_s == "2":
                    delete_card()

                elif action_s == "0":
                    break

                else:
                    print("您输入不正确，请重新输入！")
            break

    else:
        print("您查询的名片不存在！")






def modify_card():
    """修改名片"""

    pass


def delete_card():
    """删除名片"""

    pass