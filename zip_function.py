#zip fun

stu_id = [5995,5996,5997,5998]
stu_name = ['sakthi','dhina','viveck']
age = [24,28,30]

overall = list(zip(stu_id,stu_name,age))
print(overall)


#unzip
product = [('mobile',101,),('books',102),('elect',103)]
proid,proname = zip(*product)
print(proid)
print(type(proid))
print(proname)


