data ={1:'Navin',2:'kiran',4:'Harsh'}
#print(data[1])
#print(data.get(3))
#print(data.get(2,'Not found'))
#print(data.get(3,'Not found'))
keys=['Navin','kiran','Harsh']
values=['JS','Python','Java']
datas=dict(zip(keys,values))#zip() in python can be used to join two files
#print(datas)
#print(datas['kiran'])
datas['Monica']=['CS']
#print(datas['Monica'])
#print(datas)
progL={'JS':'Atom','CS':'VS','Python':['Pycharm','Spyder'],'Java':{'JavaSE':'Netbeans','JavaEE':'Eclipse'}}
#print(progL['Python'][1])
#print(progL['Java']['JavaSE'])
data2=data.copy()
del data2[2]
#print(data2)
#print(data)
data2.update({3:'Neha'})#update() function is used to add new items to a dictionary
#print(data2.items())
#print(data2.keys())
print(data2.values())


