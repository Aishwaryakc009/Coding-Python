"how many times you need to multiply 2 by 2 until the result becomes ≥ num1."



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

"""n = int(input("Input: "))

count = 0
power = 1

while power < n:
    power *= 2
    count += 1

print(count)"""