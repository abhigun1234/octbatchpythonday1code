#tuple
'''myaddress=('hinjewadi','phase1','near kpit')
print(type(myaddress))
myaddress[0]='jjjj'''

#dict

mydict={'key':'value'}
print(mydict['key'])
myinfo={'adress':'hinjewadi'}
print(myinfo['adress'])
myinfo['adress']='balewadi'
print(myinfo['adress'])

#set data



myset=set()
myset.add(1)
myset.add(11)
myset.add(111)
myset.add(1111)
myset.add(11)
print(myset)

# set operation

loteryno={1,2,3,4,5,6,7,8,9}
myno={1,5}
print(loteryno.intersection(myno))

myset={1,2,3,4,5}
newset={1,2,3,4,5}
print(myset.union(newset))
value=myset.difference_update(newset)
print(value)