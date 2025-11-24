money = input("How much money you make per hour?")
hour_of_work =input("How much hours you worked this week?")

try:
    money = float(money)
except ValueError:
    print("Please put a valid number.")
    exit()


try:
    hour_of_work = int(hour_of_work)
except ValueError:
    print("Please put a valid number.")
    exit()

weekly_payement = money * hour_of_work

print(f"Your payment this week will be: ${weekly_payement}")

