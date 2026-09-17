def call_by_val(x):
    x=x*2
    return x

def call_by_ref(b):
    b.append("D")
    return b

a = ["E"]
num = 9

updated_num = call_by_val(num)
updated_list = call_by_ref(a)

print("Updated value after call_by_val:", updated_num)
print("updated list after call_by_ref:", updated_list)

print(a)
print(num)
