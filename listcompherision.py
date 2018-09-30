'''my_list=[0,1,2,3,4,5]
equallist=[x  for x in range(0,5)]
print(equallist)
# squar
square =[x*x for x in range(0,100)]
print(square)
oddnolist=[x for x in range(0,100) if x%2!=0]
print(oddnolist)
pepole_you_know=['Rolf','jhon','raj']
normalised=[person.lower() for person in pepole_you_know]
print(normalised)'''
'''a={1,2,3}
b={1,2}
#print(a.difference(b))
print(a-b)
#print(a.difference_update(b))
print(b-a)'''
A = {'a', 'c', 'g', 'd','h','f'}
B = {'a', 'c', 'g', 'd'}
'''
When you run the code,

result will be None
A will be equal to A-B
B will be unchanged
'''

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)
