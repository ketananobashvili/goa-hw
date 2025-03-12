#5) მომხმარებელს შემოატანინე მთელი რიცხვი. იმ შემთხვევაში, თუ ეს რიცხვი არის ლუწი და ამავდროულად არის 10-ზე მეტი, დაბეჭდე True. ყველა სხვა შემთხვევაში False. 

num1 = int(input("enter a number: "))


if num1 % 2 == 0 and num1 > 10:
    print(True)
else:
    print(False)