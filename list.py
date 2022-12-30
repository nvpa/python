list=['us','india','china','brazil']
#print(list)
#print(list[0:3])
#print(range(len(list)))
#print(list[0:-1])
#print(list[0:-4]) empty list
#list.append('1')
#print(list)
#list.insert(1,'dep')
#print(list)
#list1=['dp','cp','hp','dell']

#list.append(list1)
#print(list)
#nest_list=[list,list1]
#print(nest_list)
#list.pop()# removwes last element or index positon of
#list.remove('us') #perticular element
#print(list)
#list.sort()
#print(list)
#l=[1,2,4,5,6,7,22,323,113,43,2,4,1]
#l.sort(reverse=False)
#print(l)
#update list with index position
#list[2]='rome'
#print(list)
#new_list=list
#print(new_list)
#print(id(list))
#print(id(new_list)) # id was same for two list
# or
#new_list=list[:]
#print(new_list)
#print(id(list))
#print(id(new_list)) # id was same for two list
## two will be same
new_list1=list.copy()
print(new_list1)
print(id(list))
print(id(new_list1)) # when we do copy address will be different
