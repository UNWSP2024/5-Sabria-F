#By: Sabria Fafach
#Date: Febuary 2, 2025
#Title: program_1.py


def kilometer_conversion(kilometers):    
    miles = kilometers*0.214
    return miles

def main ():
    kilometers= float(input("Enter a number of kilometers to converted to miles:"))
    miles=kilometer_conversion(kilometers)
    print(f"The number of miles is {miles:.2f} mi.")
    return main

main()