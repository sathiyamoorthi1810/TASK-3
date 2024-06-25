#list comprehension
'''
lst = [5,10,25,12,4]
lst2 = []

for i in lst:
    sqr = i**i
    lst2.append(sqr)
print(lst2)
'''
'''
lst = [5,10,25,12,4]
lst2 = [i*i for i in lst]
print(lst2)
'''

lst = [5,10,25,12,4]
a = [num for num in lst if num%5 == 0]
print(a)




