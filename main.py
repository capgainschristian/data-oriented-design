import random

from employee_data.employee_data import EmployeeData
from controllers.employee_controller import EmployeeDataController

employee_data = EmployeeData()
controller = EmployeeDataController(employee_data)

foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Burgers", "Salad", "Ice Cream", "Steak", "Curry", "Sushi"]

first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Emma", "William", "Olivia",
               "James", "Sophia", "Daniel", "Ava", "Joseph", "Mia", "Thomas", "Charlotte", "Christopher", "Amelia"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

for i in range(100):
    id = i + 1
    name = generate_name()
    salary = round(random.uniform(30000, 150000), 2)
    department = random.choice(employee_data.available_departments)
    favorite_food = random.choice(foods)
    
    employee_data.add_employee(id, name, salary, department, favorite_food)


print(controller.get_all_employees())
print(controller.get_total_employees())
print(controller.get_average_salary())
print(controller.find_highest_lowest_salary())
print(controller.get_total_salaries())
print(employee_data.lookup_employee(23))