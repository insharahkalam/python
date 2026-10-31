products = ["Laptop", "Mouse", "Keyboard", "Headphones", "Monitor"]
prices = [85000, 1500, 4500, 7000, 35000]
stock = [3, 10, 5, 0, 2]

total = 0

# First Product
p1 = input("Enter first product: ").title()
q1 = int(input("Enter quantity: "))

if p1 == "Laptop":
    price1 = 85000
    available1 = 3
elif p1 == "Mouse":
    price1 = 1500
    available1 = 10
elif p1 == "Keyboard":
    price1 = 4500
    available1 = 5
elif p1 == "Headphones":
    price1 = 7000
    available1 = 0
elif p1 == "Monitor":
    price1 = 35000
    available1 = 2
else:
    price1 = 0
    available1 = 0
    print("Product does not exist!")

if price1 > 0:
    if q1 <= 0:
        print("Invalid quantity!")
    elif available1 == 0:
        print(p1, "is Out of Stock!")
    elif q1 > available1:
        print("Insufficient stock!")
    else:
        amount1 = price1 * q1
        total = total + amount1
        stock[products.index(p1)] = available1 - q1
        print(p1, "purchased successfully!")

# Second Product
p2 = input("\nEnter second product: ").title()
q2 = int(input("Enter quantity: "))

if p2 == "Laptop":
    price2 = 85000
    available2 = stock[0]
elif p2 == "Mouse":
    price2 = 1500
    available2 = stock[1]
elif p2 == "Keyboard":
    price2 = 4500
    available2 = stock[2]
elif p2 == "Headphones":
    price2 = 7000
    available2 = stock[3]
elif p2 == "Monitor":
    price2 = 35000
    available2 = stock[4]
else:
    price2 = 0
    available2 = 0
    print("Product does not exist!")

if price2 > 0:
    if q2 <= 0:
        print("Invalid quantity!")
    elif available2 == 0:
        print(p2, "is Out of Stock!")
    elif q2 > available2:
        print("Insufficient stock!")
    else:
        amount2 = price2 * q2
        total = total + amount2
        if p2 == "Laptop":
            stock[0] = stock[0] - q2
        elif p2 == "Mouse":
            stock[1] = stock[1] - q2
        elif p2 == "Keyboard":
            stock[2] = stock[2] - q2
        elif p2 == "Headphones":
            stock[3] = stock[3] - q2
        elif p2 == "Monitor":
            stock[4] = stock[4] - q2
        print(p2, "purchased successfully!")

# Third Product
p3 = input("\nEnter third product: ").title()
q3 = int(input("Enter quantity: "))

if p3 == "Laptop":
    price3 = 85000
    available3 = stock[0]
elif p3 == "Mouse":
    price3 = 1500
    available3 = stock[1]
elif p3 == "Keyboard":
    price3 = 4500
    available3 = stock[2]
elif p3 == "Headphones":
    price3 = 7000
    available3 = stock[3]
elif p3 == "Monitor":
    price3 = 35000
    available3 = stock[4]
else:
    price3 = 0
    available3 = 0
    print("Product does not exist!")

if price3 > 0:
    if q3 <= 0:
        print("Invalid quantity!")
    elif available3 == 0:
        print(p3, "is Out of Stock!")
    elif q3 > available3:
        print("Insufficient stock!")
    else:
        amount3 = price3 * q3
        total = total + amount3

        if p3 == "Laptop":
            stock[0] = stock[0] - q3
        elif p3 == "Mouse":
            stock[1] = stock[1] - q3
        elif p3 == "Keyboard":
            stock[2] = stock[2] - q3
        elif p3 == "Headphones":
            stock[3] = stock[3] - q3
        elif p3 == "Monitor":
            stock[4] = stock[4] - q3

        print(p3, "purchased successfully!")

# Discount
if total > 100000:
    discount = total * 0.20
elif total > 50000:
    discount = total * 0.10
elif total > 20000:
    discount = total * 0.05
else:
    discount = 0

# Extra Discount
if (p1 == "Laptop" or p2 == "Laptop" or p3 == "Laptop") and (
    p1 == "Mouse" or p2 == "Mouse" or p3 == "Mouse"
):
    extra_discount = (total - discount) * 0.05
else:
    extra_discount = 0

final_bill = total - discount - extra_discount

# Delivery
if final_bill > 70000:
    delivery = 0
else:
    delivery = 500

final_amount = final_bill + delivery

# Most Expensive Product
expensive = ""

if price1 > 0 and q1 > 0 and q1 <= 3:
    expensive = p1
    highest = price1
else:
    highest = 0

if price2 > highest and q2 > 0:
    highest = price2
    expensive = p2

if price3 > highest and q3 > 0:
    highest = price3
    expensive = p3

# Receipt
print("\n========== FINAL RECEIPT ==========")
print("Product 1:", p1)
print("Product 2:", p2)
print("Product 3:", p3)
print("Subtotal:", total)
print("Discount:", discount)
print("Extra Discount:", extra_discount)
print("Delivery Charges:", delivery)
print("Final Amount:", final_amount)
print("Most Expensive Product:", expensive)

print("\nUpdated Stock:", stock)
