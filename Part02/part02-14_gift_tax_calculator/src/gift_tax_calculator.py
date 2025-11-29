# Write your solution here

# promt use for value of gift
gift = float(input("Value of gift: "))

#defining variables
tax = 0

# Condition statements evaluating tax
if gift < 5000:
    print("No tax!")
elif 5000 <= gift < 25000:
    tax += (100 + (gift - 5000) * 0.08)
    print(f"Amount of tax: {float(tax)} euros")
elif 25000 <= gift < 55000:
    tax += (1700 + (gift - 25000) * 0.1)
    print(f"Amount of tax: {float(tax)} euros")
elif 55000 <= gift < 200000:
    tax += (4700 + (gift - 55000) * 0.12)
    print(f"Amount of tax: {float(tax)} euros")
elif 200000 <= gift < 1000000:
    tax += (22100 + (gift - 200000) * 0.15)
    print(f"Amount of tax: {float(tax)} euros")
else:
    tax += (142100 + (gift - 1000000) * 0.17)
    print(f"Amount of tax: {float(tax)} euros")
