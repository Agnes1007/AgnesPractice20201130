import cards_tools_b

while True:

    # 显示功能
    cards_tools_b.show_menu()

    action_str = input("请选择您希望操作的功能：")
    print("您选择的操作是 %s" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools_b.cards_new()
        if action_str == "2":
            cards_tools_b.show_cards()
        if action_str == "3":
            cards_tools_b.search_cards()

    elif action_str == "0":
        print("退出系统！")
        break

    else:
        print("您的输入有误，请重新输入！")