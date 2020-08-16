import random #导入模块
num=5
answer=random.randint(1,10)#生成一个随机数
print(answer)

while num>0:
    temp = input("what your number:\n")
    temp = int(temp)
    if temp == answer:
        print("you are right")
        break#跳出循环
    else:
        if temp < answer:
            print("small")
        else:
            print("big")
        num=num-1
print("game over")