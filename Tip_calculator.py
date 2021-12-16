# It is a simple tip calculator
#You have to give Amount as well as the tip
#it returns you total amount calculated

print("Welcome to the tip calculator.")
amount = float(input("What was the total bill? Rs."))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
t1 = tip/100
total = t1*amount + amount
f = round(total,2)
print(f"Amount to pay:Rs.{f}")