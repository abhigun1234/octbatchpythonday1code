# list

'''mylist=[0,1,2,3,4]
print(mylist)
mylistcom=[x  for x in range(0,5) ]
print(mylistcom)
mysquareofno=[x*x for x in range(0,100)]

print(mysquareofno)

myoddnolist=[x for x in range(0,100) if x%2==1 ]
print(myoddnolist)
'''
myknownpepole=['Rajesh','Ramesh','Vikas']
for person in myknownpepole:
    print(person.upper())


listofpepole=[person.upper() for person in myknownpepole]
print(listofpepole)