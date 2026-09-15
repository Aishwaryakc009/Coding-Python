"AES number "

def is_armstrong(n):
    original = n
    n=abs(n)
    power = len(str(n))
    total = 0

    while n>0:
        digit=n%10
        total += digit**power
        n//=10
    return total ==abs(original)
n= int(input(" enter :"))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("not AES" )