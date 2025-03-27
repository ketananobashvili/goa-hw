#4) გადაუარეთ სტრინგს for loop-ით და სტრინგში მხოლოდ ლუწ ინდექსებზე მდგომი ასოები დაბეჭდეთ 

name = "keta nanobashvili"
num = 0
for i in name:
    if num % 2 == 0:
        print(i)
    num = num + 1