def gcd(a,b):

    while b:
        a,b=b,a%b
    return abs(a)
a=int(input("enter a :"))
b=int(input("enter b:"))
print(gcd(a,b))