import csv



def read():
    company = []
    numEmployees = []
    ceoSalary = []
    with open("Assignments/2024/companies.csv", "r") as file:
        data = csv.reader(file)
        for row in data:
            company.append(row[0])
            numEmployees.append(row[1])
            ceoSalary.append(row[2])
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
        print(f"The company with the highest CEO salary is {company[highestSalaryPos]}. The selected company was {company[position]}. The difference between CEO salaries was {difference}.")



def findMaxPos(list):
    maxPos = 0
    for i in range(0, len(list)):
        if list[i] > max:
            maxPos = i
    return maxPos




company, numEmployees, ceoSalary = read()
findDifference(company, ceoSalary)