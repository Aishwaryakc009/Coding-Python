"Counting number of digits in a given number"

def count_digits(n):
    n=abs(n)
    if n==0:
        return 1
    count=0

    while n>0:
        n//=10
        count+=1
    return count

n =int(input("enter :"))
print(count_digits(n))
