import math
#Variable
name = 'hungpv'
age = 22
print('I am ' + name + ' ' +  str(age))
print('Could check data type by type: ' + str(type(name)))
# Multiple assignment:
# name, age = 'hungpv', 22

# String methods
name = 'hung'
print(len(name))
print(name.find('un'))
print(name.isdigit())
print(name.isalpha())
print(name.count('h'))
print(name * 3)

# Type casting

x = 1
y = 2.0
z = '3'

print(int(y))
print(str(x))
print(float(z))
# Note: 15.5 can not cast by int() -> Throw error

# user input (command line)
# input return string -> Have to cast data type
username = input('Enter user name: ')
print(username)

# Math functions

pi = 3.14
print(round(pi)) #expect 3
print(math.ceil(pi)) #expect 4
# Notice: math.sqrt - pow - abs - max - min - ...


# String sclicing
name = 'Phan Van Hung'
firstName = name[0:8]
lastName = name[9:]
nameWithStep = name[::2]
reversedName = name[::-1]
print(firstName)
print(lastName)
print(nameWithStep)
print(reversedName)

