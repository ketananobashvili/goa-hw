#1) ცვლადში შეინახეთ თქვენი სახელი. შემდეგ ინდექსინგის მეშვეობით ეკრანზე გამოიტანეთ სტრინგიდან ყველა ის ასო, რომელიც არის ხმოვანი.

#vowel = "aeiou"
#name = "keta"

#lt = ""

#for index in name:
    #for i in vowel:
#         if index == i:
#             lt += index
# print(lt)


str1 = "keta"

vowel = "aeiou"


for i in str1:
    if i in vowel:
        print(i)
