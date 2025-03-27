#4) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ მომხმარებლის მიერ შემოტანილი პაროლი არ დაემთხვევა თქვენს პაროლს, გამოუტანეთ "Incorrect password. Try again". იმ შემთხვევაში თუ ეს პაროლები ერთმანეთს დაემთხვევა გამოიტანეთ "Correct password. You have successfully logged in." (გააკეთეთ While ციკლით, არ გამოიყენოთ if else statement-ები.);



password = "20071030"

    
password2 = input("Enter password: ")

while password2 != password:
    print("Incorrect password. Try again.")
    password2 = input("Enter password: ")

print("Correct password. You have successfully logged in.")