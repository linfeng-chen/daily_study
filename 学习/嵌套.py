#列表嵌套字典，字典嵌套列表，字典嵌套字典
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
# 在实际操作中，大量的字典被随机生成，并被加入列表中
aliens=[]
for alien in range(30):
    new_alien={'color':'blue','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
# 对字典进行部分修改
for alien in aliens[:3]:
    if alien['color']=='blue':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
for alien in aliens[:5]:
    print(alien)
print("...")
# 将列表存在字典中
pizza={'crust':'thick',
       'toppings':['mushrooms','extra cheese'],
       }
print('You ordered a '+pizza['crust']+'-crust pizza'+
      'with the following toppings:')
for topping in pizza['toppings']:
    print('\t'+topping.title())
# 在字典中储存字典
user={
    'chenlinfeng':{
        'first':'chen',
        'last':'linfeng',
        'address':'guizhou',
    },
    'luaiyin':
        {
            'first':'lu',
            'last':'aiyin',
            'address':'guangdong',
        },
}
user['shengming']={
    'first':'sheng',
    'last':'ming',
    'address':'space',
}
for username,user_info in user.items():
    print("\nUsername: "+username)
    full_name=user_info['first']+' '+user_info['last']
    address=user_info['address']
    print('\t'+full_name.title())
    print('\t'+address.title())
