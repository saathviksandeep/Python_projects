grade = int(input("Enter your grade percentge (Round to the nearest whole number): "))

if grade >= 92:
    print("Your grade is an A")
elif grade >= 89 and grade <92:
    print("Your grade is an A-")
elif grade >=87 and grade <89:
    print("Your grade is an B+")
elif grade >= 83 and grade <87:
    print("Your grade is an B")
elif grade >=80 and grade <83:
    print("Your grade is an B-")
elif grade >= 77 and grade <80:
    print("Your grade is an C+")
elif grade >=73 and grade <77:
    print("Your grade is an C")
elif grade >=70 and grade <73:
    print("Your grade is an C-")
elif grade >=67 and grade <70:
    print("Your grade is an D+")
elif grade >=63 and grade <67:
    print("Your grade is an D")
elif grade >=60 and grade <63:
    print("Your grade is an D-")
elif grade >=57 and grade <60:
    print("Your grade is an F+")
else:
    print("Your grade is an F")

