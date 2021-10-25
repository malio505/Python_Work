#This program displays costs per foot at bulk pricing for fiber optic cable.

name =(input("Please enter company name: "))
print("Welcome!", name)
feet = float(input("Please enter the feet of fiber optic cable: "))

if feet > 100:
    sum = 0.80 * feet
if feet > 250:
    sum = 0.70 * feet
if feet > 500:
    sum = 0.50 * feet
else:
    sum = 0.87 * feet

print(f"Your cost for fiber optic cable is ${sum}.", name)