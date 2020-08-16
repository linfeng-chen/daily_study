##使用if语句对列表进行操作
# 检查特殊元素
# 确定列表非空
name=['bob',"tom","lihua","alin","admin"]
name.clear()
if name:
    for nam in name:
        if nam=="admin":
            print("Hello admin, would you like to see a status report")
        else:
          print("Hello "+nam+","+"thank you for logging in again")
else:
    print("we need to find some users!")

current_users=["bob","tom","lihua","alin","admin"]
new_users=["tom","admin","mimi","wawa","yuyu"]
for name in new_users:
    if name.lower() in current_users:
        print("Please write again!")
    else:
        print("It's ok!")
