year = input("Enter a number to determine if it was a leap year. ")
year_i = int(year)
switch = 1
if year_i % 4 == 0:
     if year_i % 100 == 0:
         if year_i % 400 != 0:
                 switch = 0
else:  
  switch = 0
if switch == 1:
    print(year + " is a leap year.")
else:
    print(year + " is not a leap year.")


