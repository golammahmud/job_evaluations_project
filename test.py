a = [5, 2, 3, 1, 4]
num=sorted(a ,reverse=True)
# print(num)

# numbers = ["1", 2, 3.0]
# print(type(numbers))
# ints = [int(item) for item in numbers]
# print(ints)

integers = [1, 2, 3]


strings = [str(integer) for integer in integers]
print(f'string:{type(strings)}')
print(f'string:{strings}')


if '8' in strings:
  print("True")
else:
    print("False")



a_string = ",".join(strings)
print(f'a_string:{a_string}')





#convert int to str

num = 10.5
 
# check  and print type of num variable
print(type(num))
 
# convert the num into string
converted_num = str(num)
 
# check  and print type converted_num variable
print(type(converted_num))