import pickle

'''# 将字典，列表转换为2进制放入文件中，用pickl模块
# 存放：pickling
# 读取：unpickling'''


my_str = [12323,"chen linfeng",2324,['sdasd']]
file_name= "../txt/my_str.pickl"
with open(file_name,'wb') as obj:
    pickle.dump(my_str,obj)

with open(file_name,'rb') as obj:
    my = pickle.load(obj)
    print(my)
