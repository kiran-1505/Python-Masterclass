1. If statements 

name = input("Enter your name ")
age = int(input("How old are you {0}? ".format(name)))
print(age)

if age>=18:
    print("You can vote")

Output: 
Enter your name Kiran
How old are you Kiran? 21
21
You can vote
*************************************

2. If and else statement

name = input("Enter your name ")
age = int(input("How old are you {0}? ".format(name)))
print(age)

if age>=18:
    print("You can vote")
else:
    print("Please comeback after {0} years".format(18-age))

Output:
Less than 18
   Enter your name Kiran
How old are you Kiran? 12
12
Please comeback after 6 years

Greater than 18
   Enter your name Kiran
How old are you Kiran? 22
22
You can vote
*************************************

3. elif statements

name = input("Enter your name ")
age = int(input("How old are you {0}? ".format(name)))
print(age)

if age < 18:
    print("You can vote")
elif age == 22:
    print("Cast your vote. You are youth")
else:
    print("Please comeback after {0} years".format(18-age))


Output:
Enter your name kiran
How old are you kiran? 22
22
Cast your vote. You are youth

*************************************

4. Write a small program that assigns the value 5 to one variable, called x, and the value 7 to another, called y.

Your program should then use an if statement to compare the values, and print out x is greater than y if x is greater, or x is smaller than y if y is greater. If x equals y, print out x equals y

x = 5
y = 7

if x>y:
    print("x is greater than y")
    
elif x==y:
    print("x equals y")
    
else:
    print("x is smaller than y")

Output:
x is smaller than y

*************************************

5.  Guessing a number Program

number = 5

print("Guess the number btw 1 and 10")
guess = int(input("Type here "))

if guess > number:
    print("Guess the lower number")
    guess = int(input("Try again "))
    if guess == number:
        print("Your guess is right")
    else:
        print("Restart again")
        
elif guess == number:
    print("Your guess is right")

else:
    print("Guess the greater number")
    guess = int(input())
    if guess == number:
        print("Your guess is right")
    else:
        print("Restart again")
Output:
Guess the number btw 1 and 10
Type here 9
Guess the lower number
Try again 5
Your guess is right

*************************************
6. and, or in conditions 

print("Enter your age: ")
age = int(input())

if age>20 and age<30:        #both condition should satisfy
    print("You are young ")

elif age>41 or age <60:      #Any one condition can be satisfied
    print("You are near to become a senior citizen")

else:
    print("Condition not satisfied")

Output:

Enter your age: 
45
You are near to become a senior citizen

or

Enter your age: 
24
You are young 

*************************************
7. Boolen operation (And, or , not)

day = input("Enter the day ")
temp = input("Enter the temperature ")
rainy = input("Is it raining (True/False) ")

if day == "Monday" and temp > '27' and not rainy:
    print("Go to swimming")
else:
    print("Don't go")

Output:
Enter the day Monday
Enter the temperature 30
Is it raining (True/False) True
Don't go

*************************************

8. in condition

animal = "Elephant"
letter = input("Enter the character ")

if letter in animal:
    print("The {} is in {}".format(letter,animal))
else:
    print("The character is not present")

Output
Enter the character e
The e is in Elephant

or 

Enter the character phant
The phant is in Elephant

or

Enter the character A   #CASE SENSITIVE
The character is not present

*************************************

9. not in condition 

animal = "Elephant"
letter = input("Enter the character ")

if letter not in animal:
    print("The {} is not in {}".format(letter,animal))
else:
    print("The character is present")

Output
Enter the character q
The q is not in Elephant

*************************************
10. if and else 

name = input("Enter the name ")
age = int(input("Enter the age "))

if age >= 18 and age < 31:
    print("{} you are welcomed to the holiday".format(name))
else:
    print("You can't enter")

Output:
Enter the name Kiran
Enter the age 22
Kiran you are welcomed to the holiday

*************************************

11. Loops (for)

parrot = "Norwegian Blue"

for character in parrot:
    print(character)

Output:
N
o
r
w
e
g
i
a
n
 
B
l
u
e

*************************************
12. Printing out all the separators in the string

number = "9,223;372:036 854,77;807"
separtors = " "

for char in number:
    if not char.isnumeric():
        separtors = separtors + char

print(separtors)

Output:
 ,;: ,;

*************************************
13. 
Write a program to print out the capital letters in the string
"Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, 
Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"

Answer: 

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)
        
*************************************
14.
Write a program to print out all the numbers from 0 to 9. Each number should print on a new line

for i in range(0,10):
    print("{}".format(i))
output:
*************************************
<<<<<<< HEAD
15. 
=======
15. Range with steps

for i in range(0,10,2):
    print("{}".format(i))

Output:
0
2
4
6
8

*************************************
16.
Nested 
>>>>>>> fedff8e (1)
