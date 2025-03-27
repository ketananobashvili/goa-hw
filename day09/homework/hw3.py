#3)მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ რიცხვები მომხმარებლის შემოტანილი რიცხვიდან 0-მდე. (მაგ. input = 3. output: 3 2 1)

num = int(input("please enter your number: "))

for i in range(num, 1, -1):
    print(i)