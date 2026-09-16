" TWO POINTER APPROACH"

def isPallindrome(x):
    x=str(x)
    left , right = 0 , len(x)-1

    while left < right:
        if x[left] != x[right]:
            return "Not a Pallindrome"

        left+=1
        right-=1
    return "Its a pallindrome"

x=int(input("enter a number:"))
print(isPallindrome(x))