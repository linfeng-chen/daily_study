def converation (c):
    num=c**4;
    return  num
# c = int(input("请输入一个数: "))
# b = converation(c)
# print("结果为:" + str(b))

a,b= eval(input("one number:"))
# if a>1:
#     print(9999)
# elif -10<a<1:
#     print(666)
# elif a<-10:
#     print(555)
# print(5555) if a < 0 else print(666)
small = a if a < 0 else b
print(small)

# a,b=map(int,input().split()       给两个元素赋值
# 输入两个字符串：
# >>> a,b=input().split()
# 使用eval()函数
# >>> a,b=eval(input())