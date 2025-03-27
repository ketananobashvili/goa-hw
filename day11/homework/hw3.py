#3) გაიხსენეთ გაკვეთილზე გაკეთებული დავალება მომხმარებლის სისტემაში შესვლის მცდელობაზე და დამოუკიდებლად გააკეთეთ იგივე while ციკლის საშუალებით.

password = "keettaa22"

password2 = input("please enter your password: ")
while password != password2:
   print("your password is incorrect: ")
   password2 = input("please enter your password: ")
print("your password is correct")
