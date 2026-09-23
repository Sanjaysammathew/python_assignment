# 2. Employee Salary Analyzer
# Accept:
# •	Employee name
# •	Basic salary
# •	Experience
# Calculate:
# •	HRA
# •	DA
# •	Gross salary
# •	Bonus based on experience
# •	Final salary category
# Use conditions and calculations.


Employee_name=input("Enter your name: ")
print(F" The Employee name is {Employee_name}")

Basic_salary=int(input("Enter your salary: "))
print(f"The basic salary is {Basic_salary}")

Employee_Experience=int(input("Enter your experience: "))
print(f"The employee Experience is {Employee_Experience}")


#calculate HRA
hra= Basic_salary*0.20

# calculate DA

da=Basic_salary*0.10

#calculate Gross Salary

Gross_salary=Basic_salary+hra+da
bonus=0
#calculate bonus based on Experience
if Employee_Experience <=2 :
    bonus=Basic_salary*0.05
elif Employee_Experience <=5 :
    bonus=Basic_salary*0.10
elif Employee_Experience <=10 :
    bonus=Basic_salary*0.20

#final_salary

final_salary=Basic_salary+bonus


# Determine salary category
if final_salary >= 100000:
    category = "High"

elif final_salary >= 50000:
    category = "Medium"

else:
    category = "Low"
    
    
print("Employee Details:")
print(f"Employee Name : {Employee_name}")
print(f"Basic Salary  : {Basic_salary:.2f}")
print(f"HRA           : {hra:.2f}")
print(f"DA            : {da:.2f}")
print(f"Gross Salary  : {Gross_salary:.2f}")
print(f"Bonus         : {bonus:.2f}")
print(f"Final Salary  : {final_salary:.2f}")
print(f"Category      : {category}")

