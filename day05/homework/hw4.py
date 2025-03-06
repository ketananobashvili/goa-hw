#5) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტშ
#farenheit = celsius * (9/5) + 32
#celsius = 5/9 * (farenheit - 32)

celsius = int(input("enter a number: "))
farenheit = celsius * (9/5) + 32
celsius2 = 5 / 9 * (farenheit - 32)
print("farenheit")