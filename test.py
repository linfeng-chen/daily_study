# -*- coding = utf-8 -*-
# @time:2020/10/10 19:06
# Author:chen linfeng
# @File:test.py


class stack:
    def __init__(self):
        self.stack = []
    def add(self, val):
        self.stack.append(val)
        return True
    def head(self):
        if len(self.stack)==0:
            print("栈为空")
        else:
            return self.stack[len(self.stack)-1]
    def pop(self):
        try:
            self.stack.pop(len(self.stack) - 1)
            return True
        except IndexError:
            print("栈为空")
    def length(self):
        return len(self.stack)

if __name__=="__main__":
    one = stack()
    str = input("")
    for i in str:
        if i =='(' or i==')':
            if one.length()==0:
                one.add(i)
            else:
                if one.head()=='(' and i==')':
                    one.pop()
                else:
                    one.add(i)
    if one.length()==0:
        print("配对成功")
    else:
        print("配对不成功")
