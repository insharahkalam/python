distance = float(input("Enter your distance in km: "))
weather = input("Enter the Weather (sunny/rainy): ")
ord_Amount = float(input("Enter YOur order amount: "))

def foodDelievery(distance, weather, ord_Amount):
    total_time = 15
    add_on = distance * 5
    total_time += add_on

    if weather == "rainy":
        total_time += 20

    if distance > 10:
        total_time += 10

    charges = 50 * distance

    if ord_Amount >= 2000:
        charges = 0

    return total_time, charges


total_time, charges = foodDelievery(distance, weather, ord_Amount)
final_amount = ord_Amount + charges

print("\n\n")
print("*" * 60)

print(f"DISTANCE: {distance}")
print(f"WEATHER: {weather}")
print(f"ORDER AMOUNT: {ord_Amount}")
print(f"DELIEVERY CHARGES: {charges}")
print(f"TOTAL TIME: {total_time}")
print(f"FINAL AMOUNT: {final_amount}")
