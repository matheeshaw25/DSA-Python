num1 = 11
num2 = num1

print("Before num2 value is updated")
print(f"Num1:{num1}")
print(f"Num2:{num2}")

print(f"Num 1 points to:{id(num1)}")
print(f"Num 2 points to:{id(num2)}")

num2 = 22


print("After num2 value is updated")
print(f"Num1:{num1}")
print(f"Num2:{num2}")

print(f"Num 1 points to:{id(num1)}")
print(f"Num 2 points to:{id(num2)}")

print("--------------------------------------------------------------------------------------------------------")

dict1 = {
    'value':11
}

dict2 = dict1

print("Before Dict 2 value is updated")
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")

print(f"Dict 1 points to:{id(dict1)}")
print(f"Dict 2 points to:{id(dict2)}")

dict2['value'] = 22

print("After Dict 2 value is updated")
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")

print(f"Dict 1 points to:{id(dict1)}")
print(f"Dict 2 points to:{id(dict2)}")