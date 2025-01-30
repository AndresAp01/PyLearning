#Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("Interest rate amount must be greater than zero")
    else:
        break

while True:
    time = float(input("Enter time in years: "))
    if time < 0:
        print("Number of years must be greater than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s is ${total:.2f}")
