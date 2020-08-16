def add(x):
    if x==1:
        return 1
    return x + add(x-1)
x=int(input("请输入一个数:"))
print(add(x))
