from employee_data.employee_data import EmployeeData
from controllers.employee_controller import EmployeeDataController

employee_data = EmployeeData()
controller = EmployeeDataController(employee_data)

employee_data.add_employee(1, "Christian", 200000)
employee_data.add_employee(2, "Bob", 60000)
employee_data.add_employee(3, "Michael", 125000)

employee_data.update_employee(2, name="John")

john = employee_data.lookup_employee(2)
print(john)

employee_data.delete_employee(3)

deleted = employee_data.lookup_employee(3)
print(deleted)
christian = employee_data.employee_name_lookup('Christian')
print(christian)

print(controller.get_all_employees())