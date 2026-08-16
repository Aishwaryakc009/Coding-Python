str1=input("Enter input:")
output=""
char=str1[0]
count=0

for ch in str1:
    if ch==char:
        count+=1
    else:
        output+=str(count)+char
        count=1
        char=ch
output+=str(count)+char
print(output)