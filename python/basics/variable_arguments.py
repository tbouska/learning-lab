def addNumbers(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


numbers_in_list = [1, 2, 3, 4, 5, 6, 7, 8, ]
numbers_in_tuple = (1, 3, 5, 7, )

print("Passing arguments directly", addNumbers(1, 2, 3, 4, 5))
print("Passing arguments as a list", addNumbers(*numbers_in_list))
print("Passing arguments as a tuple", addNumbers(*numbers_in_tuple))

# and this will fail, because argument unpacking operator `*` is missing
print("Incorrectly passing arguments as a list ", addNumbers(numbers_in_list))
"""
>>>
Traceback (most recent call last):
  File "C:/User/bob/Git/src/gitlab.com/tbouska-learning/py/variable_arguments.py", line 15, in <module>
    print("Incorrectly passing arguments as a list ", addNumbers(numbers_in_list))
  File "C:/User/bob/Git/src/gitlab.com/tbouska-learning/py/variable_arguments.py", line 4, in addNumbers
    sum += i
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
"""
