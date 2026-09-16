"print the number which has appeared only once"

list=input("enter numbers:")

l1=[]

for num in list:
    if list.count(num)==1:
        l1.append(num)

print(l1)





print(list)
print(type(list))