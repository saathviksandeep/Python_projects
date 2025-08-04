year=int(input("Enter year:"))

num=(year-1930)/4-2

if num!=int(num):
    print("There is no World Cup in", year,".")
elif year==1942 or year==1946:
    print("These World Cups were cancelled due to war.")
else:
    if num==1:
        print("In", year,"the 1st World Cup will have taken place.")
    elif num==2:
        print("In", year, "the 2nd World Cup will have taken place.")
    elif num==3:
        print("In", year, "the 3rd World Cup will have taken place.")
    else:
        print("In", year, "the", num,"th World Cup will have taken place.")
