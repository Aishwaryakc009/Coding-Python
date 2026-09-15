"finding no of trailing zeros"
n=int(input("Enter:"))
count=0
while n>0 and n%10==0:
    count+=1
    n//=10
print(count)