name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
disease = input("Enter patient disease: ")

print("\n----- Patient Details -----")
print("Patient Name:", name)
print("Patient Age:", age)
print("Disease:", disease)

if age > 40:
    print("Suggested Medicine: High Dosage")
elif age < 40:
    print("Suggested Medicine: Low Dosage")
else:
    print("Age is 40. Consult a doctor for dosage.")
