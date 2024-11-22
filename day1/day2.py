my_list = ["a", "b", "c", "h", "e"]
list2 = ["f", "g", "h"]
my_list[3] = "d"
my_list.append('f')
print(my_list)
my_list.pop(0)
print(my_list)
my_list.extend(list2)
print(my_list)

my_list.remove("e")
print(my_list)
tuple1 = (1,2,3,4)
tuple1.append(5)
list3 = [2,2,3,4,4,7,7]
print(list(set(list3)))
set1 = {1,3,4,5,5, 6, 6, 7}

my_list = ["cricket", "football", "basketball", "tennis"]
my_list.sort(reverse=True)
print(my_list)

student = {"name": "abhinav", "number": "23445464", "address": "kathmandu", "subjects": ["physics", "math", "english"]}
print(student["subjects"])
student["grade"] = 12
my_number = student.pop('number')
print(student)
print(my_number)
a = 9

if a == 1:
    print("Value of a is 1")
elif a == 2:
    print("Value of a is 2")
elif a == 3:
    print("Value of a is 3")
else:
    print("Value of a is neither 1 nor 2 nor 3")

a = 9

match a:
    case 1:
        print("The value of a is 1")
    case 2:
        print("The value of a is 2")
    case 3:
        print("The value of a is 3")
    case 4:
        print("The value of a is 4")
    case _:
        print("The value of a is neither 1 nor 2 nor 3 nor 4")

student = {"name": "abhinav", "number": "23445464", "address": "kathmandu", "subjects": ["physics", "math", "english"]}
for i in student:
    print(i)
print("The loop is completed")

print(student.values())

for i in range(1, 101, 2):
    print(i)