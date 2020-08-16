love = 9
sum = 0
while love > 1:
    sum = sum + love
    love = love - 1
print( sum )
print(type(sum))
## break,continue 语句作用与C语言相同
## else 语句
day = 1;
while day <= 7:
    answer = input("今天学了吗？")
    if answer != "s":
        break
    day +=1
else:
    print("good boy")
print()#换行
## else 在循环中的作用：检测循环的退出状态