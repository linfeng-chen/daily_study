'''使用模块json来保存数据'''
#储存：json.dump(),读取：json.load()
import json

number= [2,2,3,4,6,8,0]
filename = 'txt/number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)

with open(filename,'r') as f_obj:
    numbers = json.load(f_obj)
print(numbers)

username = input("What is your name? ")

filename = 'txt/username.json'
with open(filename,'w') as us:
    json.dump(username,us)
    print("Your name is remembered")

try:
    with open(filename,'r') as obj:
        username = json.load(obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as us:
        json.dump(username, us)
        print("Your name is remembered")
else:
    print("Welcome back, "+username)