#Ashutosh chaurasia
# Batch 5
#0176AL231033

#program 1
check_num=input('Enter a no : ')
check_num=int(check_num)
if check_num>0:
    print(f'The number ({check_num}) is positive')
elif check_num<0:
    print(f'The number ({check_num}) is negetive')
else:
    print('The number is zero')


#program 2
even_odd=int(input('Enter a no :'))
if even_odd%2==0:
    print('Given number is even')
else:
    print('given number is odd')

#program 3
year=int(input('ENter  the year : '))
if year%100==0 and year%400==0 and year%4==0:
    print('This is a leap year')
elif year%4==0 and year%100!=0:
    print('This is a leap year')
else:
    print('Not a leap year')

#program 4
num1=int(input('enter a no : '))
num2=int(input('enter a no : '))
if num1>num2:
    print(f'{num1}is greater')
elif num1==num2:
    print('numbers are equal')
else :
    print(f'{num2} is greater')

    #program 5 

age=int(input('enter a no : '))
if age>=18:
    print('The person is eligible to vote')
else:
    print('You are underaged')


#program 6
vowels='aeiou'
alphabet=input('enter a letter : ')
if len(alphabet) != 1:
    print("Please enter a single character.")
if alphabet in vowels:
    print('The letter is vowel')
else:
    print('THe letter is consonant')
    
#program 7
div_5=int(input('enter a no : '))
if div_5%5==0:
    print('no is divisible by 5')
else:
    print('not divisible by 5')

#program 8

digit=input('enter a no : ')
if len(digit)==1:
    print('SIngle digit no')
elif len(digit)==2:
    print('two digit no')
else:
    print('more than two digit no')

#program 9
marks=int(input('enter your marks : '))
if marks<40:
    print('fail')
else:
    print('pass')

#program 10

multiple=int(input('enter a no : '))
if multiple%3==0 and multiple%7==0:
    print('dibisible by 3 and 7')
else:
    print('not divisible by 3 and 7')


#program 11
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a >= b) and (a >= c):
    greatest = a
elif (b >= a) and (b >= c):
    greatest = b
else:
    greatest = c
print("The greatest number is:", greatest)

#program12
p_age = int(input("Enter age: "))


if p_age < 13:
    category = "Child"
elif p_age >= 13 and age <= 19:
    category = "Teenager"
elif p_age >= 20 and age <= 59:
    category = "Adult"
elif p_age >= 60:
    category = "Senior"
else:
    category = "Invalid age"

print("The person is classified as:", category)

#program13

marks = float(input("Enter marks: "))


if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks <= 89:
    grade = "B"
elif 50 <= marks <= 74:
    grade = "C"
elif 35 <= marks <= 49:
    grade = "D"
elif 0 <= marks < 35:
    grade = "Fail"
else:
    grade = "Invalid marks"

print("The assigned grade is:", grade)

#program 14

a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))


if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        triangle_type = "Equilateral triangle"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"
    else:
        triangle_type = "Scalene triangle"
else:
    triangle_type = "Not a valid triangle"

print("The triangle type is:", triangle_type)

#program 15


char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter a single character.")
else:
    if char.isupper():
        print("The character is an uppercase letter.")
    elif char.islower():
        print("The character is a lowercase letter.")
    elif char.isdigit():
        print("The character is a digit.")
    else:
        print("The character is a special symbol.")

#program 16

units = float(input("Enter the number of units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"Total electricity bill: ₹{bill}")

#program 17

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a >= b:
    if a >= c:
        if a >= d:
            largest = a
        else:
            largest = d
    else:
        if c >= d:
            largest = c
        else:
            largest = d
else:
    if b >= c:
        if b >= d:
            largest = b
        else:
            largest = d
    else:
        if c >= d:
            largest = c
        else:
            largest = d

print("The largest number is:", largest)


#program 18

year = int(input("Enter a year: "))

if year % 100 == 0:
    print(f"{year} is a century year.")
 
    if (year % 400 == 0):
        print(f"{year} is also a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a century year.")

# program 19

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi}")
print("BMI category:", category)

#program 20

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b:
    if a <= c:
        smallest = a
    else:
        smallest = c
else:
    if b <= c:
        smallest = b
    else:
        smallest = c

print("The smallest number is:", smallest)

#program 21


for num in range(100, 1000):
    #
    a = num // 100          
    b = (num // 10) % 10    
    c = num % 10            
    
    sum_cubes = a**3 + b**3 + c**3
    
    if num == sum_cubes:
        print(num)

#PROGRAM 22

n = int(input("Enter how many primes: "))
num = 2  
count = 0

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1

#program 23
numbers=[]
sum=0
for i in range(1, 501):
    for j in str(i):
        sum=sum+int(j)

    if i % 3 == 0 and sum>10 :
        print('Numbers from 1 to 500 divisible by 3 with digit sum <= 10:')
    else :
        print("Numbers from 1 to 500  are not divisible by 3 with digit sum <= 10:")
#program 24

n = 4  

for i in range(1, n + 1):
   
    for j in range(n - i):
        print(" ", end="")
   
    for k in range(2 * i - 1):
        print("*", end="")
   
    print()

#program 25

s = input("Enter a string: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
found = True

for ch in alphabet:
    if ch not in s:
        found = False
        break

if found==True:
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")
    #program 26

for i in range(2, 99): 
   
    is_i_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_i_prime = False
            break

    is_i2_prime = True
    for j in range(2, int((i + 2)**0.5) + 1):
        if (i + 2) % j == 0:
            is_i2_prime = False
            break

    if is_i_prime and is_i2_prime:
        print(f"({i}, {i + 2})")

#program 27
num = int(input("Enter a number: "))

sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)

if num % sum_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is NOT a Harshad number.")

#program28
n = int(input("Enter the number of rows: "))

for i in range(n):
    
    for j in range(n - i - 1):
        print(" ", end="")

    
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1) 

    print()  

#program 29

n = int(input("Enter n: "))

sum_series = 0
for i in range(1, n + 1):
    sum_series += i**2

print(f"The sum of the series is: {sum_series}")

#program 30
num = int(input("Enter a number: "))
sum_factorial = 0


for digit in str(num):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum_factorial += fact


if sum_factorial == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is NOT a Strong number.")

num = int(input("Enter a number: "))

original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    i = 2
is_prime=True
while i * i <= reverse:
    if reverse % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
        print(f"{reverse} is prime.")
else:
    print(f"{reverse} is NOT prime.")


#program 32

total_sum = 0

while total_sum <= 100:
    num = int(input("Enter a number: "))

    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
    
    total_sum += sum_digits
    print(f"Sum of digits so far: {total_sum}")

print("The sum of digits of all numbers entered is now greater than 100.")

#program 33
num = int(input("Enter a number: "))

temp = num
is_duck = False
while temp > 0:
    digit = temp % 10
    if digit == 0:
        is_duck = True
    temp //= 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10

if is_duck and first_digit != 0:
    print(f"{num} is a Duck number.")
else:
    print(f"{num} is NOT a Duck number.")

#program 34
num = int(input("Enter a number: "))
n = num
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    temp = n
    sum_squares = 0
    
    while temp > 0:
        digit = temp % 10
        sum_squares += digit * digit
        temp //= 10
    n = sum_squares

if n == 1:
    print(f"{num} is a Happy number.")
else:
    print(f"{num} is NOT a Happy number.")


#program 35
num = int(input("Enter a number: "))
n = num
i = 2  
largest_prime = 0

while i * i <= n:
    if n % i == 0:
        largest_prime = i
        while n % i == 0:
            n //= i
    i += 1


if n > 1:
    largest_prime = n

print(f"The largest prime factor of {num} is {largest_prime}.")

#program 36
while True:
    s = input("Enter a string: ")
    
    if s == s[::-1]:
        print(f"'{s}' is a palindrome.")
        break
    else:
        print(f"'{s}' is not a palindrome. Try again.")

#program 37
num = int(input("Enter a number: "))
n = num

while n >= 10:  
    sum_digits = 0
    
    while n> 0:
        sum_digits += n % 10
        n //= 10
    n = sum_digits

print(f"The digital root of {num} is {n}.")
# program 38

n = int(input("Enter a number: "))

print("Collatz sequence:")

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:  
        n //= 2
    else:           
        n = 3 * n + 1

print(1)  

#program 39
num = int(input("Enter a number: "))

square = num * num
n = square

digits = 0

while num > 0:
    digits += 1
    num //= 10

right = square % (10 ** digits)
left = square // (10 ** digits)

# check Kaprekar condition
if left + right == num:
    print("it is a Kaprekar number.")
else:
    print("it is NOT a Kaprekar number.")

# program 40

balance = 0  

while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
    elif choice == "4":
        print("Exiting... Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please enter 1-4.")












