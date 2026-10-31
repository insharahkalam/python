
# IF conditions Implementation

name = input("Enter customer name: ")
units = int(input("Enter electricity units: "))

if (units > 0 and units <= 100):
    print("Rate Per Unit: Rs. 10")
    
elif units > 101 and units <= 200:
    print("Rate Per Unit: Rs. 15")

elif units > 201 and units <= 300:
    print("Rate Per Unit: Rs. 20")
    
else:
    print("Rate Per Unit: Rs. 25")

