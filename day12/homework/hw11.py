#12) დააკვირდით მოცემულ flowchart-ს, ახსენით მისი მუშაობის პრინციპი. მისი მიხედვით შეადგინეთ პროგრამა და დაწერეთ რა შედეგს გამოიტანს კოდი იმ შემთხვევაში როცა მომხმარებელი არის 14 წლის და არ არის სტუდენტი.

age = 14
is_student = False

if age < 18:
    if is_student:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount")