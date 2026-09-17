"""Input =[a,a,b,b,c,a,,c,b,c,a]
output = [a:4,b:3,c:3]"""

str1=input("enter :")
list1=str1.split(',')
visited=[]
final_list=[]
for ch in list1:
    if ch not in visited:
        final_list.append(f"{ch}:{list1.count(ch)}")
        visited.append(ch)
print(",".join(final_list))