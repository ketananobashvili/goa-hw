#დაწერეთ პროგრამა, რომელიც მომცმარებლს მოსთხოვს, რომ შემოიტანოს დადებითი რიცხვი. თუ მომხმარებელი შემოიტანს უარყოფით რიცხვს ან ნულს, პროგრამამ უნდა მოსთხოვოს რიცხვის თავიდან შემოტანა

user_num = int(input("enter a number: "))
while user_num <= 0:
    print("your entered number is not valid. try again")
    user_num = int(input("enter a number: "))
    print("your number was positive. ")