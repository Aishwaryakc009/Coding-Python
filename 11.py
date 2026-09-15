" find two nums which adds up to target "

nums= eval(input("enter array of ints:"))
target = int(input("Enter target:"))

output=[]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target and len(output)==0:
            output.append(i)
            output.append(j)


print("Output :", output)