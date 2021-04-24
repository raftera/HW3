while True:
    try:
        year = int(input("Enter a number to determine if it was a leap year. "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    else:
        break
    
switch = 1
if year % 4 == 0:
     if year % 100 == 0:
         if year % 400 != 0:
                 switch = 0
else:  
  switch = 0
if switch == 1:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")


