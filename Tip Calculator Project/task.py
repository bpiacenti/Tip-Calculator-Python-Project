print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_calc = (tip / 100) + 1
total = (bill / people)  * tip_calc

print(f"Each person should pay: {round(total, 2)}")
