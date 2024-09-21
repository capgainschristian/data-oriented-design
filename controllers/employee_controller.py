class EmployeeDataController:
    def __init__(self, employee_data):
        self.employee_data = employee_data

    def get_all_employees(self):
        employees = []
        for i in range(len(self.employee_data.names)):
            employees.append(self.employee_data.names[i])

        return employees