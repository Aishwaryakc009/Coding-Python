"Input is a list , output is a list which contains { 1st element , sum of all other elements}"

L1=list(map(int,input("enter a list elements separated by spaces:").split()))
output=[]
output.append(L1[0])
sum1=0
for  i in range(1,len(L1)):
    sum1+=L1[i]
output.append(sum1)
print(output)