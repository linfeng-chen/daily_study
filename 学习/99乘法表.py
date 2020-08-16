i=1
while i <= 9:
    j=1
    while j <= i:
        print(j,'*',i ,'=',j*i,end=" ")#end 用来取消换行
        j +=1
    print()
    i +=1

for i in "my girl":
    print(i)
i = 0
while i < len("my girl"):
    print("my girl"[i])
    i += 1
## range
##range(start,stop)
# range(start,stop,step)
sum=0
for i in range(900,10001,5):
    sum +=i
    i +=1
print( sum )