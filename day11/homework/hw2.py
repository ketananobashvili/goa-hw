#2) შექმენით Number guess game, while ციკლების გამოყენებით.

num = 4
num2 = int(input("please enter your number: "))
while num != num2:
    print("your number is incorrect")
    num2 = int(input("enter another number"))
print("your number is correct: ")
