matric = float(input("Enter your Matric marks (%): "))
inter = float(input("Enter your Intermediate marks (%): "))
entry_test = float(input("Enter your Entry Test marks (out of 100): "))
interview = float(input("Enter your Interview marks (out of 100): "))

def universityAdmission(matric, inter, entry_test, interview):

    merit = (matric * 0.20) + (inter * 0.30) + (entry_test * 0.40) + (interview * 0.10)

    if matric < 60 or inter < 65 or entry_test < 50:
        status = "Rejected"

    elif merit >= 85:
        status = "Scholarship + Admission"

    elif merit >= 70:
        status = "Admission Confirmed"

    elif merit >= 60:
        status = "Waiting List"

    else:
        status = "Rejected"

    return merit, status


merit, status = universityAdmission(matric, inter, entry_test, interview)


print("\n")
print("*" * 60)

print(f"MATRIC MARKS: {matric}%")
print(f"INTERMEDIATE MARKS: {inter}%")
print(f"ENTRY TEST MARKS: {entry_test}")
print(f"INTERVIEW MARKS: {interview}")
print(f"FINAL MERIT: {merit:.2f}%")
print(f"ADMISSION STATUS: {status}")

print("*" * 60)
