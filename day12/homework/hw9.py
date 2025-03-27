#10) რთული:
#მომხმარებელს შემოატანინეთ რიცხვი და დაწერეთ პროგრამა, რომელიც შეამოწმებს ეს რიცხვი მარტივია თუ არა. (მარტივია რიცხვი, თუ მას მხოლოდ ორი გამყოფი აქვს). მინიშნება: გამოიყენეთ For loop და % გამყოფი ოპერატორი, ასევე აუცილებლად დაგჭირდებათ პროგრამაში Boolean ნიშვნელობების გამოყენება (True და False).


number = int(input("Enter number: "))
count = 0

for divider in range(2, (number // 2) + 1):
    if number % divider == 0:
        count = count + 1
        break

if count == 0:
    print("Number is prime")
else:
    print("NUmber is not prime")