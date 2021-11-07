print("WELCOME TO JEMS PIZZA")
size = input("WHAT SIZE DO YOU WANT PLEASE? S, M , L:   ")
add_pepperoni = input("DO YOU WANT PEPPERONI PLEASE? Y, N:   ")
extra_cheese = input("DO YOU WANT EXTRA CHEESE? Y, N:    ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill =+ 3

if extra_cheese == "Y":
    bill += 1

print(f"YOUR FINAL BILL IS ${bill}")