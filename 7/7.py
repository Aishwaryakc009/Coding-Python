f1 = open("employee.txt", mode='r')
f2 = open("result.txt", mode='w')

modified_data=[]
data=f1.readlines()
header=data[0]
modified_data.append(header)

for record in data[1:len(data)+1]:
    my_list = record.split("|")
    salary = float(my_list[2])

    if salary > 35000 :
        bonus = 2000
        modified_data.append(f"{my_list[0]}|{my_list[1]}|{float(my_list[2])+bonus}\n")

    else:
         modified_data.append(f"{my_list[0]}|{my_list[1]}|{float(my_list[2])}\n")

f2.writelines(modified_data)
f1.close()
f2.close()