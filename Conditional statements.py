####
# conditional statements - 1

x = int(input('Enter a value:'))

if x%2 == 0:
    print('EVEN')
else:
    print('ODD')

####
# conditional statements - 2

text_line = input('enter line of text:')
my_str = input('enter a string:')

if my_str in text_line:
    print('True')
else:
    print('False')

####
# conditional statements - 3

vowels =  ["a","e","i","o","u"]

word = input("type a word: ")

if vowels in word:
     print ("The word contains vowel")
else:
     print ("There is no vowel in the word")

####
# conditional statements - 4

vowels =  ["a","e","i","o","u"]

alphabets = input("type an alphabet: ")

if alphabets in vowels:
     print ("Vowel")
else:
     print ("Constant")

####
# conditional statements - 5

x = float(input('enter a number for x:'))
y = float(input('enter a number for y:'))

z = x-y
if z <= .001:
     print('close')
else:
     print('not close')

####
# conditional statements - 6

x =int(input('enter age of x: '))
y =int(input('enter age of y: '))
z =int(input('enter age of z: '))

if x>y and x>z:
    print('x is oldest')
elif y>x and y>z:
    print('y is oldest')
else:
    print('z is oldest')
    
if x<y and x<z:
    print('x is youngest')
elif y<x and y<z:
    print('y is youngest')
else:
    print('z is youngest')

####
# conditional statements - 7    

digits =input('enter the value:')

even_sum=0
multiple_odd = 1
for x in digits:
    x = int(x)
    if x%2 == 0:
        even_sum += x
    if x%2 == 1:
        multiple_odd = multiple_odd * x
        
print('sum of even numbers:',even_sum)
print('multiple of odd numbers:',multiple_odd)

####
# conditional statements - 8

year = int(input('enter any year:'))

if year%400 == 0:
    print ('this is a leap year')
else:
    print('not a leap year')

####
# conditional statements - 9

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")

####
# conditional statements - 10

x = int(input('enter starting range value:'))
y = int(input('enter ending range value:'))

for i in range(x , y):
    if i%7 == 0:
        print('values divisible by 7:',i)
    elif i%5 == 0:
        print('values multiple by 5:',i)

####
# conditional statements - 11

temp = input("Enter units of temperature: ")

if ((temp == 'c') or (temp == 'C')):
    x = float(input("Enter the value of temp in °C: "))
    far = (x * (9/5) +32)
    print ("The temperature in Fahrenheit is", far,"°F")
if ((temp == 'f') or (temp == 'F')):
    y = float(input("Enter the value of temp in °F: "))
    cel = ((y-32) *(5/9))
    print("The temperature in Celsius is", cel, '°C')