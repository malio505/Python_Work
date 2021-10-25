# A program showing an investiment doubling at a given interest rate.

def Invest():

    rate = int(input("Enter the annualized interest rate: "))
    Invest = int(input("Enter the initial investment amount: "))

    year = 0
    principal = 1

    while principal < (principal * 2):
        interest = (principal * rate * 1)/100
        principal = principal + interest
        year += 1
    print("The number of years it takes for your investment to double is",year)

Invest()
