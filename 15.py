"LCM"

def gcd(a,b):
    while b:
        a,b =b,a%b
    return abs(a)
def lcm(a,b):
    if a==0 or b==0:
        return 0
    return abs(a//gcd(a,b)*b)
a= int(input("enter a:"))
b=int(input("enter b:"))
print(lcm(a,b))