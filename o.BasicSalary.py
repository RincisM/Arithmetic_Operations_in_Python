salary = int(input("Enter the Basic pay: "))
HRA = (15/100)*salary
TA = (5/100)*salary
GrossSalary = HRA + TA + salary
print("House Rental Allowance:", HRA)
print("Travel Allowance:", TA)
print("The Gross salary of the user is:", GrossSalary)