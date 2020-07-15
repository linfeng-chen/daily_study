import re
def sum_numbers(text: str) -> int:
    text=text.split()
    # print(text)
    num=[]
    for i in text:
        if ((i[0]).isdigit())==True and i[len(i)-1].isdigit()==True:
            num.append(i)
    # print(num)
    text=[int(i) for  i in num]
    return sum(text)





num="3 sras2 dsd32sdf 2232 sdsd"
x=sum_numbers(num)
print(x)