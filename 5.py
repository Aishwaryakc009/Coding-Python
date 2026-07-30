"a2b3c6 ---> aabbbccccc"
class Solution:
   def numvar(self, str1: str):
        output=" "
        for char in str1:
            if char.isalpha():
                     var=char
            else:
                      num= int(char)
                      output+=var*num
        return output
sol=Solution()
print(sol.numvar("a3c5n8"))

"""
str1= input()
output=""
for char in str1:
  if char.isalpha():
     var=char
  else:
     num = int(char)
     output+=var*num
print(output)
"""
