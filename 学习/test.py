name=["tom","mike","bob"]
print(name)
print("I want invest " + name[0].title()+"、"+ name[1].title()+" and "+name[2].title()+"to join my meet!")
print(name[1].title()+" can't come.")
name[name.index("mike")]="alien"
print(name)
name.insert(0,"linfeng")
print(name)
name.insert(int(len(name)/2),"job")
name.append("lucy")
print(name)
x=name.pop(-1)
print("sorry ".title()+x.title())
print(name)
del name[0:2]#可用切片思想删除一段
print(name)
name.clear()
print(name)
name=["beijing","yuzhou","shanghai","taitanxing","shenming"]
print(name)
print(sorted(name))
print(name)
print(sorted(name,reverse=True))
name.reverse()
print(name)
name.reverse()
print(name)
name.sort()
print(name)
name.sort(reverse=True)
print(name)
#使用列表时避免索引错误
for i in range(1,21):
    print(i,end=" ")
num=[i for i in range(1,1000001)]
print("\n"+str(max(num)))
print(min(num))
print(sum((num)))
num=[i*3 for i in range(1,11)]
print(num)

num_1=num[:]
print(num)
num_1.append(999)
print(num)
print(num_1)
num_1=num  #使用此方法在改变num_1的时候num同样也会改变
print(num_1)
num_1.append(999)
print(num)
print(num_1)

car = 'subaru'
print("is car=='subaru'? i prediict True")
print(car=='subaru')