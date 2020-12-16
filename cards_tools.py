# 记录所有名片的字典
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email":email_str}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户名片建立成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():

    """显示全部"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片信息，请使用新增功能添加名片！")
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name,end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 1.遍历名片列表，依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

        # for k in card_dict:
        #     print(card_dict[k], end="\t")
        # print("")


def search_card():
    """查询名片
    """

    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要查询的姓名：")

    # 2.遍历列表，查询要搜索的名片，如果没有找到，统一给用户提示
    for cards_dict in card_list:
        if cards_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"],
                                            cards_dict["phone"],
                                            cards_dict["qq"],
                                            cards_dict["email"]))

            # 针对找到的名片记录执行修改和删除的操作
            deal_card(cards_dict)

            break
    else:
        print("查询的名片不存在！")


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """

    print(find_dict)
    action_str = input("请输入对名片的操作："
                       "1：修改/ 2：删除/ 0：返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息，回车不修改

    :param dict_value: 字典原有的值
    :param tip_message: 提示用户输入的信息
    :return: 如果用户输入了内容，返回内容，如果没有输入内容，返回字典原有的值
    """

    # 1.提示用户输入内容
    action_str = input(tip_message)
    # 2.针对用户输入的内容作出判断，如果输入了内容，直接返回结果
    if len(action_str) > 0:
        return action_str
    # 3.如果没有输入内容，返回字典中原有的值
    else:
        return dict_value
