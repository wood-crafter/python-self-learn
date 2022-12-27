# import math
# #Variable
# name = 'hungpv'
# age = 22
# print('I am ' + name + ' ' +  str(age))
# print('Could check data type by type: ' + str(type(name)))
# # Multiple assignment:
# # name, age = 'hungpv', 22

# # String methods
# name = 'hung'
# print(len(name))
# print(name.find('un'))
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('h'))
# print(name * 3)

# # Type casting

# x = 1
# y = 2.0
# z = '3'

# print(int(y))
# print(str(x))
# print(float(z))
# # Note: 15.5 can not cast by int() -> Throw error

# # user input (command line)
# # input return string -> Have to cast data type
# username = input('Enter user name: ')
# print(username)

# # Math functions

# pi = 3.14
# print(round(pi)) #expect 3
# print(math.ceil(pi)) #expect 4
# # Notice: math.sqrt - pow - abs - max - min - ...


# # String sclicing
# name = 'Phan Van Hung'
# firstName = name[0:8]
# lastName = name[9:]
# nameWithStep = name[::2]
# reversedName = name[::-1]
# print(firstName)
# print(lastName)
# print(nameWithStep)
# print(reversedName)


# # If statement

# age = int(input('Enter your age:'))

# if age > 35:
#   print('Old ass!')
# elif age > 18:
#   print('Adult!')
# else:
#   print('Kid!')


# # Logical operator

# heigh = int(input('Enter your heigh in cm: '))
# if not(heigh > 160 or heigh < 100):
#   print('Short ass')
# if (heigh >= 160 and heigh <= 175):
#   print('Medium ass')
# if (heigh > 175 and heigh < 200):
#   print('Tall ass')
# if (heigh >= 200 or heigh < 100):
#   print('Monster ass')


# # Loops

# # While work just as usual
# for i in range(3, 8, 2):
#   print('Im in loop with num: ' + str(i))
# for i in 'Should print out as row':
#   print(i, end='')


# # List

# foods = ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'pudding', 3, 4]
# foods[0] = 'sushi'

# foods.append('ice cream')
# foods.remove('hotdog')
# print(foods.pop())
# print('List:')

# for x in foods:
#   print(x)


# Tuple: a collection which is ordered and unchangeable used to group together related data

student = ('Phan Van Hung', 22, 'male')
print(student.count('male'))
print(student.index('male'))

