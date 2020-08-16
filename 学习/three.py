
# x=input()
# print(temp,x)
# print(temp == x)

num=5
while num>0:
    temp = input("what your number:\n")
    temp = int(temp)
    if temp == 7:
        print("you are right")
        break#跳出循环
    else:
        if temp < 7:
            print("small")
        else:
            print("big")
        num=num-1
print("game over")