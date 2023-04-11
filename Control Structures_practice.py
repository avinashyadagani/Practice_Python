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

####
####
# Special use cases

x = int(input(" number of classes held:"))
y = int(input(" number of classes attended:"))

# percentage of classes attended = per_atd
per_atd = (y/x)*100

if per_atd < 75:
    result = input("Do you have a medical cause (Y or N): ")
    if result == 'Y':
        print("your are eligible to write exam")
    else:
        print("your are not eligible to write exam")
if per_atd >= 75:
    print("your are eligible to write exam")

####
####
# Looping statements 

## 1

i = 0

while i <= 5:
    print (i)
    i+=1

## 2

my_str = input('Enter a word: ')

i = 1

while i <= len(my_str):
    print(my_str[-i])
    i+=1

## 3

num = int(input(" Enter a number: "))

i = 1

while i <= num:
    if num % i== 0:
        print (i)
    i +=1

## 4

num = int(input(" Enter a number: "))

i = 1
fact = 1

while i <= num:
        fact = fact*i
        i = i + 1
print("The factorial of", num, "is", fact)

## 5

num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number:'))

a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("Hcf of", a, "and", b, "is", num1)

## 6

product = 1
sum = 0
count = 1

while True:
    
    user_input = input('Enter a number: ')
    if user_input == 'q':
        break
    user_input = int(user_input)
    
    sum = sum + user_input
    product  = product * user_input
    count = count + 1
    
print('Average:', sum/count)
print('product:', product)

## 7

num = int(input("Enter a number:"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")