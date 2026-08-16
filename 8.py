var = input("Input:")
var=var.split()
num1=int(var[0])
result=2
count=0

while result<num1:
    result  = result*2
    count += 1
    if result >= int(num1):
        break 
print(count)

