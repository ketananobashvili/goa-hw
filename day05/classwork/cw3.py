#BONUS:
#შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ სახელს და ასაკს, შემდეგ შეამოწმეთ ასაკი, თუ ასაკი >= 18 დაუბეჭდეთ რომ მას შეუძლია შევიდეს კლუბში, სხვა შემთხვევაში დაუბეჭდეთ რომ არ შეუძლია.

name = input("enter your name: ")
age = int(input("enter your age: "))

if age >= 18: 
    print("you can enter the club: ")
else:
     print("you can't enter the club")