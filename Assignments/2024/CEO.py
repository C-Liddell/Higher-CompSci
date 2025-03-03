import csv



def read():
    company = []
    numEmployees = []
    ceoSalary = []
    with open("Assignments/2024/companies.csv", "r") as file:
        data = csv.reader(file)
        for row in data:
            company.append(str(row[0]))
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
    return company, numEmployees, ceoSalary


def findDifference(company, ceoSalary):
    chosenCompany = str(input("Enter a company: "))
    found = False
    highestSalaryPos = findMaxPos(ceoSalary)
    for i in range(0, len(company)):
        if company[i] == chosenCompany:
            found = True
            position = i
    
    if found == True:
        difference = ceoSalary[highestSalaryPos] - ceoSalary[position]
        print(f"""
The company with the highest CEO salary is {company[highestSalaryPos]}. 
The selected company was {company[position]}. 
The difference between CEO salaries was {difference}.
              """)
    else:
        print("Company not found.")



def findMaxPos(list):
    maxValue = 0
    maxPos = 0
    for i in range(0, len(list)):
        if list[i] > maxValue:
            maxValue = list[i]
            maxPos = i
    return maxPos



def countEmployees(numEmployees):
    mostEmployeePos = findMaxPos(numEmployees)
    count = 0
    for i in range(0, len(numEmployees)):
        if numEmployees[i] >= numEmployees[mostEmployeePos]*0.9:
            count += 1
    print(f"""
The highest number of employees at a single company is {numEmployees[mostEmployeePos]}.
The number of companies who employ within 10% of that figure is {count}.
          """)



company, numEmployees, ceoSalary = read()
findDifference(company, ceoSalary)
countEmployees(numEmployees)