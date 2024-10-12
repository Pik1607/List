#immutable_var = ("Рост питона",38,"попугаев",True,"вес питона",38.5,"жирных попугаев",False)
#print(immutable_var)
#immutable_var [2] ='слонов'
#print(immutable_var)
# кортеж не поддерживает изменения элементов, остается неизменным, используется как хранилище

mutable_list = ["Рост питона",38,"попугаев",True,"вес питона",38.5,"жирных попугаев",False]
mutable_list [2] = 'крокодила'
mutable_list [6] = 'кроликов'
mutable_list.pop(-1)
mutable_list.remove(True)
mutable_list [1]=1.5
print(mutable_list)