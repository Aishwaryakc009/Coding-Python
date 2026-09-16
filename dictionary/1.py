"""Input : {'orange':'fruit','carrot':'veggie','banana':'fruit'}
output: {'fruit':['orange','banana'],'veggie':'carrot'}"""

dict= {'orange':'fruit','carrot':'veggie','banana':'fruit'}
output={}

for ele in dict:
    if dict[ele] not in output:
        output[dict[ele]]=[ele]
    else:
        output[dict[ele]].append(ele)
print(output)