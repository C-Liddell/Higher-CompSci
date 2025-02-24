import csv

company = []
numEmployees = []
ceoSalary = []

with open("Assignments/2024/companies.csv", "w") as file:
    reader = csv.reader(file)
    for row in reader:
