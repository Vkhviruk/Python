name = "Victoria"
lastname = "Khviruk"
age = 16
if type(name) == type(lastname):
    print(type(name))
else:
    print("Змінні мають різні типи даних")
list=[name, lastname]
print(" ".join(list))
if type(age) == type(lastname):
    print("type age = type lastname")
if type(age) != type(lastname):
    print("type 'age' ≠ type 'lastname'")
