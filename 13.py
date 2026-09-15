"factorial of a number"

def fact(n):
    if n==0 or n==1:
      return 1 
    elif n==2 :
      return 2
    else:
       for i in range(2,n+1): 
          return n *fact(n-1)

n=int(input("enter a number:"))
print(fact(n))

