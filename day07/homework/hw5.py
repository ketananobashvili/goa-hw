#4) მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

#• იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
#• თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
#• თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
#• ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F"

num1 = int(input("enter a number: "))


if num1 >= 90:
    print("A")
elif num1 >= 70 and num1 < 90:
    print("B")
elif num1 >= 50 and num1 < 70:
    print("C")
else:
    print("F")