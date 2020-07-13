def build_user(name,**infomation):
    '''创建一个字典用来存储用户信息'''
    peoson={}
    peoson['name']=name.title()
    for key,value in infomation.items():
        peoson[key.title()]=value
    print(peoson)
