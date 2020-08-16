def get_formatted_name (first,last,middle=''):
    if middle:
        full_name = first.title() + ' ' + middle + ' ' + last.title()
    else:
        full_name = first.title()+" "+last.title()
    return full_name

# print("按q退出!")
# while True:
#     first = input("输入你的姓：")
#     if first=='q':
#         break
#     last = input("输入你的名：")
#     if last =='q':
#         break
#     name = get_formatted_name(first,last)
#     print(name)