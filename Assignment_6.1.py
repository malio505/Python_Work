#A program that converts miles to kilometers.

#Input from the user
def main():
    miles = float(input("Enter the distance in miles: "))
    conv_fac = 1.60934 #converson factor
    #Calculating how many kilometers
    kilometers = miles * conv_fac
    print("The distance in kilometers is: ", kilometers)

main() 