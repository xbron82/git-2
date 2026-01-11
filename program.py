import random as r 

r_number = r.randint(1, 100)
u_number= int(input("enter a number"))

new_num=r_number+u_number
print("The random number is:", r_number)
print("The sum of the random number and your number is:", new_num)

if new_num % 2 == 0:
    print("The sum is an even number.")
else:
    print("The sum is an odd number.")