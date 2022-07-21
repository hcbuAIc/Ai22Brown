choice = 0
while True:
    I = str(input("select with a number \n hours to minutes:1 \n minutes to hours:2 \n:"))
    if (I == "1" or I == "2"):
        break



if (choice == "1"):
    x = int(input("hours:"))
    print(x*60, "minutes")
else:
    x = int(input("minutes:"))
    print(x/60, "hours")