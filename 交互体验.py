#input()工作原理
# message = input("Tell me something that you want to tell me: ")
# print(message)
# print(type(message))
# 函数input 接收一个参数，即向用户显示的提示或说明
# 使用while 函数来处理列表或字典
# 在列表之间移动元素
unconfirmed_users=['bob','tom','jike']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print('Verifying user: '+current_user.title() )
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# 删除包含特定值的所有列表元素
pets=['dog','cat','dag','rabbit','goldfish','dog']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)

# 使用用户输入来填充字典
user={}
flag=True
while flag:
    name=input("请输入名字: ")
    age=input("请输入你的年龄: ")
    user[name]=age
    respond=input("是否继续？: ")
    if(respond=='no'):
        break
print(user)