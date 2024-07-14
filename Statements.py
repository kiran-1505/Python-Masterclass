If statements 

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

  If and else statement

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

