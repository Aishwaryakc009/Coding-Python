""" need to remove one char from a string so it will get matched to the words in the given array , and finally return the count of the strings matched with comparing string . """

def equalization(n,m,s,t):
    count =0
    s1=[]
    for ch in s:
        s1.append(ch)
    print(s1)
    for i in range(n):
        char = s1.pop(i)
        for word in t:
            if "".join(s1)==word:
                count=count+1
        s1.insert(i,char)
    return count
print(equalization(5,4,'abcde',['abcd','bcde','acde','abnb']))
