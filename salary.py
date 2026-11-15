
salary = int(input("Enter your salary: "))

def calculate_bonus(salary):
    """Calculate bonus according to base salary."""
    if salary >= 50000:
        bonus = salary * 0.20
    else:
        bonus = salary * 0.10

    return bonus


def calculate_tax(total_salary):
    """Calculate tax according to total salary."""
    if total_salary >= 60000:
        tax = 2000
    else:
        tax = 0

    return tax


def salary_calculator(base_salary):
    """Calculate complete salary details."""
    bonus = calculate_bonus(base_salary)

    total_salary = base_salary + bonus

    tax = calculate_tax(total_salary)

    salary_after_tax = total_salary - tax

    return {
        "Base Salary": base_salary,
        "Bonus": bonus,
        "Total Salary": total_salary,
        "Tax": tax,
        "Salary After Tax": salary_after_tax
    }


result = salary_calculator(salary)

print("\nSalary Breakdown")
print("Base Salary:", result["Base Salary"])
print("Bonus:", result["Bonus"])
print("Total Salary:", result["Total Salary"])
print("Tax:", result["Tax"])
print("Salary After Tax:", result["Salary After Tax"])
