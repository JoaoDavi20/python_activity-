# Inputs

money = input("How much money you make per hour?")
hour_of_work =input("How much hours you worked this week?")

# Error recogniton

try:
    money = float(money)
except ValueError:
    print("Please put a valid number for money to hour")
    exit()

try:
    hour_of_work = int(hour_of_work)
except ValueError:
    print("Please put a valid number for hours you work per week")
    exit()

# Calculation

weekly_payement = money * hour_of_work

# Output

print(f"Your payment this week will be: ${weekly_payement}")

