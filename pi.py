import math

limit = 30
while True:
    digits = input("How many digits of pi would you like? ")
    if not digits.isdigit():
        print("Enter a number.")
    else:
        digits = int(digits)
        if digits > limit:
            print("Enter a smaller number.")
        else:
            pi = round(math.pi, digits)
            break

print(pi)
