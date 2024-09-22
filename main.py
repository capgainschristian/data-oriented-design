from employee_data.employee_data import EmployeeData
from controllers.employee_controller import EmployeeDataController

employee_data = EmployeeData()
controller = EmployeeDataController(employee_data)

employee_data.add_employee(1, "Christian", 200000, "IT", "wild wings")
employee_data.add_employee(2, "Bob", 60000, "HR", "pizza")
employee_data.add_employee(3, "Michael", 125000, "Sales", "pho")
employee_data.add_employee(4, "John", 80000, "HR", "pasta")
employee_data.add_employee(5, "Randy", 73000, "IT", "paneer")
employee_data.add_employee(6, "Lisa", 110000, "Sales", "wild wings")
employee_data.add_employee(7, "Rachael", 175000, "Sales", "steak")

employee_data.update_employee(2, name="John")

john = employee_data.lookup_employee(2)
print(john)

employee_data.delete_employee(3)

deleted = employee_data.lookup_employee(3)
print(deleted)
christian = employee_data.employee_name_lookup('Christian')
print(christian)

print(controller.get_all_employees())
print(controller.get_total_employees())
print(controller.get_average_salary())
print(controller.find_highest_lowest_salary())